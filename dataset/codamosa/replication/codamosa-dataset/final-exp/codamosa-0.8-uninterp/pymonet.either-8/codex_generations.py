

# Generated at 2022-06-14 03:16:49.372464
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    class Person:

        def __init__(self, name: str, age: int) -> None:
            self.name = name
            self.age = age

        def __eq__(self, other: object) -> bool:
            return isinstance(other, Person) and\
                self.name == other.name and\
                self.age == other.age

    person = Person('John', 28)

    assert Left(person) == Left(person)
    assert Right(person) == Right(person)
    assert Left(person) != Right(person)


# Generated at 2022-06-14 03:16:53.373950
# Unit test for method case of class Either
def test_Either_case():
    def error(e):
        return e

    def success(e):
        return str(e)

    assert Left(1).case(error, success) == 1
    assert Right(1).case(error, success) == '1'

# Unit tests for method ap of class Either

# Generated at 2022-06-14 03:16:57.199468
# Unit test for method case of class Either
def test_Either_case():
    """
    Case of function from Either class.
    """
    assert Right(2).case(lambda value: 2 * value, lambda value: value / 2) == 1
    assert Left(4).case(lambda value: 2 * value, lambda value: value / 2) == 8



# Generated at 2022-06-14 03:17:11.312512
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left_1 = Left('abc')
    left_2 = Left('abc')
    right_1 = Right('abc')
    right_2 = Right('abc')

    assert left_1 == left_2
    assert right_1 == right_2
    assert left_1 != right_1



# Generated at 2022-06-14 03:17:29.355430
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """Unit test for method __eq__ of class Either"""

    func1 = lambda arg: arg + arg
    func2 = lambda arg: arg + arg

    assert Left(1).__eq__(Left(1))
    assert not Left(1).__eq__(Left(2))
    assert not Left(1).__eq__(Right(1))
    assert Left(func1).__eq__(Left(func1))
    assert not Left(func1).__eq__(Left(func2))
    assert not Left(func1).__eq__(Right(func1))
    assert Right(1).__eq__(Right(1))
    assert not Right(1).__eq__(Right(2))
    assert not Right(1).__eq__(Left(1))
    assert Right(func1).__eq__(Right(func1))

# Generated at 2022-06-14 03:17:33.279332
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right(1) != Left(1)
    assert Left(1) != Right(1)


# Generated at 2022-06-14 03:17:37.659141
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Either(1) != None
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    assert Either(1) != Left(1)
    assert Either(1) != Right(1)


# Generated at 2022-06-14 03:17:46.161838
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left = Left(1)
    right = Right(2)
    other_left = Left(1)
    other_right = Right(2)
    different_right = Right(3)

    assert left == left
    assert right == right

    assert left == other_left
    assert right == other_right

    assert left != right
    assert right != left

    assert right != different_right
    assert left != different_right



# Generated at 2022-06-14 03:17:49.104591
# Unit test for method case of class Either
def test_Either_case():
    assert Left(1).case(error=lambda x: x + 2, success=lambda x: x + 10) == 3
    assert Right(1).case(error=lambda x: x + 1, success=lambda x: x + 10) == 11


# Generated at 2022-06-14 03:17:50.852871
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    either = Right(1)
    either2 = Right(1)
    assert either == either2



# Generated at 2022-06-14 03:17:58.768277
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    def foo():
        return 'foo'

    assert either.value.to_lazy() == Lazy(foo)
    assert either.value.to_lazy().force() == 'foo'



# Generated at 2022-06-14 03:18:03.594973
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest
    from pymonet.lazy import Lazy

    assert Left('test').to_lazy() == Lazy(lambda: 'test')
    assert Right('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 03:18:15.411318
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe

    # Arrange
    box = Box('fds')

    # Act
    lazy_box = box.to_lazy()
    lazy_either = Either.to_lazy()
    lazy_try = Try.to_lazy()
    lazy_maybe = Maybe.just(7).to_lazy()

    # Assert
    assert isinstance(lazy_box, Lazy)
    assert isinstance(lazy_either, Lazy)
    assert isinstance(lazy_try, Lazy)
    assert isinstance(lazy_maybe, Lazy)
    assert lazy_box.value() == box.value

# Generated at 2022-06-14 03:18:18.518887
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN
    either = Right(1)

    # WHEN
    result = either.to_lazy()

    # THEN
    assert result.is_deferred() is True
    assert result.value() == 1



# Generated at 2022-06-14 03:18:20.961227
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().force() == 1
    assert Right(1).to_lazy().force() == 1

# Generated at 2022-06-14 03:18:23.647268
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(10).to_lazy().get() == 10
    assert Right(10).to_lazy().get() == 10


# Generated at 2022-06-14 03:18:27.621454
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Test to_lazy with Either"""
    left = Left('Error')
    right = Right(1)

    assert left.to_lazy() == Lazy(lambda: 'Error')
    assert right.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:18:29.992592
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:18:37.535508
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either('test').to_lazy() == Lazy(lambda: 'test')
    assert Either(Left(10)).to_lazy() == Lazy(lambda: 10)
    assert Either(Right(10)).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:18:40.705364
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(7).to_lazy() == Lazy(lambda: 7)
    assert Either('Pymonet').to_lazy() == Lazy(lambda: 'Pymonet')


# Generated at 2022-06-14 03:18:48.547902
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:18:56.575309
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    @get_elapsed
    def f(a):
        return a + 5

    assert_that(
        Either.Right(5).to_lazy(),
        is_(equal_to(Lazy(lambda: 5)))
    )
    assert_that(
        Either.Left(5).to_lazy(),
        is_(equal_to(Lazy(lambda: 5)))
    )

    assert_that(
        f(Either.Right(5).to_lazy().get()),
        is_(equal_to(10))
    )
    assert_that(
        f(Either.Left(5).to_lazy().get()),
        is_(equal_to(10))
    )



# Generated at 2022-06-14 03:18:58.202204
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5) == Either(5).to_lazy()



# Generated at 2022-06-14 03:19:05.650262
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy_list import LazyList

    assert Left(None).to_lazy() == Lazy(lambda: None)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Right(LazyList([1, 2, 3])).to_lazy() == Lazy(lambda: LazyList([1, 2, 3]))
    assert Left(LazyList([1, 2, 3])).to_lazy() == Lazy(lambda: LazyList([1, 2, 3]))


# Generated at 2022-06-14 03:19:08.477497
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:19:21.334375
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Test with Left
    value = 'hello'
    left = Left(value)

    assert value == left.to_lazy().value()

    # Test with Right
    value = 'world'
    right = Right(value)

    assert value == right.to_lazy().value()


# Generated at 2022-06-14 03:19:25.597719
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Trying to convert Either<int> to Lazy

    :returns: assertion error if test is failed
    :rtype: AssertionError
    """
    assert Lazy(lambda: 1) == Right(1).to_lazy()


# Generated at 2022-06-14 03:19:31.535174
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left

    right = Right(1)
    lazy = right.to_lazy()
    assert lazy == Lazy(lambda: 1)

    left = Left(1)
    lazy = left.to_lazy()
    assert lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:36.308106
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Either(1).to_lazy()

    assert lazy == Lazy(lambda: 1)



# Generated at 2022-06-14 03:19:38.420044
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().get_value() == 1

# Generated at 2022-06-14 03:19:54.310530
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    Right(3).to_lazy() == Lazy(lambda: 3)
    Left(3).to_lazy() == Lazy(lambda: 3)



# Generated at 2022-06-14 03:20:01.324221
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(5).to_lazy() == Right(5).to_lazy()
    assert Either(5).to_lazy().value() == 5
    assert Either('A').to_lazy() == Left('A').to_lazy()
    assert Either('A').to_lazy().value() == 'A'


# Generated at 2022-06-14 03:20:04.345551
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Unit tests for method ap of class Either

# Generated at 2022-06-14 03:20:06.427055
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().force() == 1
    assert Left(1).to_lazy().force() == 1

# Generated at 2022-06-14 03:20:09.139158
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.Right(1).to_lazy() == Lazy(lambda: 1)
    assert Either.Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:20:18.677540
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Left(1).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy() == Left(1)
    assert lazy.call_count == 1

    lazy = Right(1).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy() == Right(1)
    assert lazy.call_count == 1


# Generated at 2022-06-14 03:20:32.019396
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda : 5)
    assert Left(4).to_lazy() == Lazy(lambda : 4)



# Generated at 2022-06-14 03:20:37.996188
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either('one').to_lazy() == Lazy(lambda: 'one')
    assert Either(Right(1)).to_lazy() == Lazy(lambda: Right(1))
    assert Either(Left(1)).to_lazy() == Lazy(lambda: Left(1))



# Generated at 2022-06-14 03:20:39.359259
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:20:45.354953
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for Either.to_lazy()
    """
    from pymonet.lazy import Lazy

    assert Left("error").to_lazy() == Lazy(lambda: "error")
    assert Right("success").to_lazy() == Lazy(lambda: "success")


# Generated at 2022-06-14 03:20:58.561758
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.functions import compose
    from pymonet.lazy import Lazy
    from operator import mul, truediv
    from functools import reduce

    # Test for Left
    divider = compose(Either.to_lazy, Left)
    assert divider('error') == Lazy(lambda: 'error')

    # Test for Right
    divider = compose(Either.to_lazy, Right)
    assert divider(1) == Lazy(lambda: 1)



# Generated at 2022-06-14 03:20:59.616110
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:06.854206
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # When Either is Right
    right_to_lazy = Right(1).to_lazy()

    # Then Both is Lazy
    assert isinstance(right_to_lazy, Lazy)
    # And value is equal
    assert right_to_lazy.get() == 1

    # When Either is Left
    right_to_lazy = Left(1).to_lazy()

    # Then Both is Lazy
    assert isinstance(right_to_lazy, Lazy)
    # And value is equal
    assert right_to_lazy.get() == 1



# Generated at 2022-06-14 03:21:08.731242
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Either(1).to_lazy(), Lazy)

# Generated at 2022-06-14 03:21:14.162917
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: Right(1))
    assert Right(1).to_lazy() == lazy
    assert Right(1).to_lazy().value() == 1

    lazy = Lazy(lambda: Left(1))
    assert Left(1).to_lazy() == lazy
    assert Left(1).to_lazy().value() == Left(1)


# Generated at 2022-06-14 03:21:15.277100
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(5).to_lazy().value() == 5



# Generated at 2022-06-14 03:21:17.894739
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:21:20.960196
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    try:
        assert Either.Left(1).to_lazy().eval() == 1
        assert Either.Right(1).to_lazy().eval() == 1
        print("test Either.to_lazy() - ok")
    except AssertionError as e:
        print("test Either.to_lazy() - fail")
        raise e


# Generated at 2022-06-14 03:21:23.652113
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Either(42).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 42


# Generated at 2022-06-14 03:21:27.608576
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    l = Lazy(lambda: Right(1).to_lazy().eval()).eval()
    r = Lazy(lambda: Right(1).to_lazy().eval()).eval()
    assert l == r

# Generated at 2022-06-14 03:21:48.643807
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right('first').to_lazy().value() == 'first'
    assert Left('second').to_lazy().value() == 'second'

# Generated at 2022-06-14 03:21:56.573812
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Right(1).to_try().to_lazy()
    assert Left(1).to_lazy() == Left(1).to_try().to_lazy()
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:21:58.979101
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:22:00.472363
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(2).to_lazy().value() == 2


# Generated at 2022-06-14 03:22:10.140256
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.
    """

    def fun():
        return 5
    assert fun() == 5

    assert Right(5).to_lazy().force() == 5
    assert Left(5).to_lazy().force() == 5

    assert Right(5).to_lazy().map(lambda x: x + 1).force() == 6
    assert Left(5).to_lazy().map(lambda x: x + 1).force() == 5

    assert Right(5).to_lazy().apply(Lazy(lambda x: x + 1)).force() == 6
    assert Left(5).to_lazy().apply(Lazy(lambda x: x + 1)).force() == 5

# Generated at 2022-06-14 03:22:14.448695
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def lazy_test(value):
        assert value == [1, 2, 3]
        print('test passed')

    Maybe.just([1, 2, 3]).to_lazy().force(lazy_test)


# Generated at 2022-06-14 03:22:17.539457
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:22:23.047499
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    number = Right(32).to_lazy()
    assert type(number) == Lazy
    assert number() == 32
    assert number.evaluated == False
    assert number.empty == False



# Generated at 2022-06-14 03:22:26.799350
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('err').to_lazy() == Lazy(lambda: 'err')
    assert Right('val').to_lazy() == Lazy(lambda: 'val')


# Generated at 2022-06-14 03:22:32.932777
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy

    assert isinstance(Left(1).to_lazy(), pymonet.lazy.Lazy)
    assert isinstance(Right(2).to_lazy(), pymonet.lazy.Lazy)
    assert Right(3).to_lazy().force() == 3
    assert Left(4).to_lazy().force() == 4



# Generated at 2022-06-14 03:23:12.403508
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()


# Generated at 2022-06-14 03:23:24.085942
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().eval() == 1
    assert Either([1, 2]).to_lazy().eval() == [1, 2]
    assert Either('1').to_lazy().eval() == '1'
    assert Either(1).to_lazy() == Either(1).to_lazy()
    assert isinstance(Either(1).to_lazy(), Lazy)
    assert isinstance(Either('1').to_lazy(), Lazy)
    assert Either({1: '1'}).to_lazy().eval() == {1: '1'}
    assert isinstance(Either({1: '1'}).to_lazy(), Lazy)
    assert Either(None).to_lazy().eval() == None
    assert isinstance(Either(None).to_lazy(), Lazy)
   

# Generated at 2022-06-14 03:23:27.135961
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(23).to_lazy().force() == 23

    assert isinstance(Either(23).to_lazy(), Lazy)
    assert not isinstance(Either(23).to_lazy(), Either)


# Generated at 2022-06-14 03:23:30.161892
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(23).to_lazy() == Lazy(lambda: 23)
    assert Right(23).to_lazy() == Lazy(lambda: 23)



# Generated at 2022-06-14 03:23:32.847631
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    foo = Right(1)
    assert foo.to_lazy() == Lazy(lambda: 1)

    bar = Left(2)
    assert bar.to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:23:43.835154
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    # WHEN
    left = Left(10)
    right = Right(10)

    # THEN
    assert isinstance(left.to_lazy(), Lazy)
    assert isinstance(right.to_lazy(), Lazy)

    assert left.to_lazy().value() == 10
    assert right.to_lazy().value() == 10



# Generated at 2022-06-14 03:23:53.667981
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(12).to_lazy().value() == 12
    assert Right(12).to_lazy().value() == 12



# Generated at 2022-06-14 03:23:57.722541
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:23:59.977155
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy()


# Generated at 2022-06-14 03:24:01.834483
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().evaluate() == 1
    assert Left('error').to_lazy().evaluate() == 'error'

# Generated at 2022-06-14 03:25:27.026782
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Given
    def sum_function(x: int, y: int) -> int:
        return x + y

    expected = Lazy(lambda: sum_function(2, 3))
    left = Left(sum_function)
    right = Right(sum_function)

    # When
    actual = left.to_lazy()
    actual_right = right.to_lazy()

    # Then
    assert expected.eval() == actual.eval()
    assert expected.eval() == actual_right.eval()



# Generated at 2022-06-14 03:25:33.956875
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left(1)
    right = Right(2)
    assert (left.to_lazy() == Lazy(lambda: 1))
    assert (right.to_lazy() == Lazy(lambda: 2))


# Generated at 2022-06-14 03:25:35.479789
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def f(): return 'test'
    either_test = Either(f)
    assert either_test.to_lazy()
    assert isinstance(either_test.to_lazy(), Lazy)

# Generated at 2022-06-14 03:25:40.353796
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    left = Either.left(1)
    right = Either.right(1)

    lazy_left = left.to_lazy()
    lazy_right = right.to_lazy()

    assert isinstance(lazy_left, Lazy)
    assert isinstance(lazy_right, Lazy)

    assert lazy_left.value is left.value
    assert lazy_right.value is right.value



# Generated at 2022-06-14 03:25:44.544370
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Either(3).to_lazy() == Maybe.just(3).to_lazy()
    assert Either(Maybe.nothing()).to_lazy() != Maybe.nothing().to_lazy()

# Generated at 2022-06-14 03:25:48.265733
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Either(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:25:55.578196
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(10).to_lazy(), Lazy)
    assert isinstance(Right(10).to_lazy().get(), int)

    assert isinstance(Left(10).to_lazy(), Lazy)
    assert isinstance(Left(10).to_lazy().get(), int)


# Generated at 2022-06-14 03:26:06.243207
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:26:16.411092
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Lazy(lambda: 3) == Either(3).to_lazy()
    assert Lazy(lambda: 'abc') == Either('abc').to_lazy()
    assert Lazy(lambda: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == Either([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]).to_lazy()
    assert Lazy(lambda: {'I': 1, 'V': 5, 'X': 10}) == Either({'I': 1, 'V': 5, 'X': 10}).to_lazy()
    assert Lazy(lambda: {10: 'a', 5: 'V', 1: 'I'}) == Either({10: 'a', 5: 'V', 1: 'I'}).to_lazy()


# Unit

# Generated at 2022-06-14 03:26:20.274041
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Either.Left(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Either.Right(Box(1)).to_lazy() == Lazy(lambda: Box(1))

