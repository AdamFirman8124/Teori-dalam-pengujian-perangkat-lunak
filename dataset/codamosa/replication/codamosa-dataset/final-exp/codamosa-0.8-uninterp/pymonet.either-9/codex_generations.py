

# Generated at 2022-06-14 03:16:43.684086
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(2) == Left(2) and Left(2) != Left(1)


# Generated at 2022-06-14 03:16:47.368246
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left = Left(1)
    right = Right(1)
    left2 = Left(1)
    right2 = Right(1)

    assert left == left2
    assert right == right2
    assert left != right
    assert right != left


# Generated at 2022-06-14 03:16:51.353631
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Either(1) == Either(1)
    assert Right(1) == Right(1)
    assert Left([1, 2]) == Left([1, 2])
    assert Right(1) != None



# Generated at 2022-06-14 03:16:57.185413
# Unit test for method case of class Either
def test_Either_case():
    assert Left(1).case(error=lambda value: "fail",
                        success=lambda value: "success") == "fail"

    assert Right(1).case(error=lambda value: "fail",
                         success=lambda value: "success") == "success"



# Generated at 2022-06-14 03:17:14.280821
# Unit test for method __eq__ of class Either
def test_Either___eq__():

    # Test when two Left instances is equal
    left = Left("abc")
    other_left = Left("abc")
    assert left == other_left

    # Test when two Right instances is equal
    right = Right("cde")
    other_right = Right("cde")
    assert right == other_right

    # Test when Left and Right instances are not equal
    assert left != right

    # Test when None is not equal to Left
    assert not left == None


# Generated at 2022-06-14 03:17:20.850495
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right(1) != Left(1)
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)



# Generated at 2022-06-14 03:17:27.234083
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Left(1) == Left(1)
    assert Left(1) != Left(2)
    assert Right(1) == Right(1)
    assert Right(1) != Right(2)
    assert Left(1) != Right(1)
    assert Left(1).to_box() == Box(1)
    assert Left(1).to_try() == Try(1, is_success=False)
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_box() == Box(1)

# Generated at 2022-06-14 03:17:32.731815
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert not Left(1) == Left(2)
    assert not Left(1) == Right(1)

    assert Right(1) == Right(1)
    assert not Right(1) == Right(2)
    assert not Right(1) == Left(1)


# Generated at 2022-06-14 03:17:36.775299
# Unit test for method __eq__ of class Either
def test_Either___eq__():

    assert Left([1, 2, 3]) == Left([1, 2, 3])
    assert Right(4) == Right(4)
    assert Left([1, 2, 3]) != Right(4)
    assert Right(4) != Left([1, 2, 3])



# Generated at 2022-06-14 03:17:44.571544
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(None).to_lazy() == Lazy(lambda: None)
    assert Right(None).to_lazy() == Lazy(lambda: None)

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:17:49.185644
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left.to_lazy(Left('left')) == Lazy(lambda: 'left')
    assert Right.to_lazy(Right('right')) == Lazy(lambda: 'right')


# Generated at 2022-06-14 03:17:51.392435
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().value() == 1
    assert Left(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:17:53.882330
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def f(x):
        return x + 5

    assert Right(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:17:58.451460
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_maybe import Maybe

    assert Either(None).to_lazy() == Lazy(lambda: None)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:18:08.508340
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.mappend import Mappend
    from pymonet.mempty import Mempty

    # Given
    value = 9
    instance = Right(value)

    # When
    actual = instance.to_lazy()

    # Then
    assert actual == Lazy(lambda: value)
    assert actual.value == value
    assert actual.is_value_created is False
    assert actual.value == actual.force()
    assert actual.is_value_created is True
    assert isinstance(actual, Mappend)
    assert isinstance(actual, Mempty)



# Generated at 2022-06-14 03:18:12.602682
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:18:16.115050
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Either(Box(Lazy(lambda: 1))).to_lazy() == Either(Lazy(lambda: Lazy(lambda: 1)))



# Generated at 2022-06-14 03:18:18.485247
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy().get_value() == 2
    assert Left('Black').to_lazy().get_value() == 'Black'


# Generated at 2022-06-14 03:18:21.798967
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    lazy = Right(Box(1)).to_lazy()
    assert lazy.value() == Box(1)



# Generated at 2022-06-14 03:18:25.406892
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:18:31.385857
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def delayed_value(val):
        def get_value():
            return val
        return get_value
    e = Right('value')
    l = e.to_lazy()
    assert l.value() == delayed_value('value')
    e = Left('value')
    l = e.to_lazy()
    assert l.value() == delayed_value('value')


# Generated at 2022-06-14 03:18:52.341740
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Either, Left, Right
    from pymonet.monad_try import Try

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)

    assert Either.to_lazy(Left(1)) == Lazy(lambda: 1)
    assert Either.to_lazy(Right(1)) == Lazy(lambda: 1)
    assert isinstance(Either.to_lazy(Left(1)), Lazy)
    assert isinstance(Either.to_lazy(Right(1)), Lazy)

    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:18:55.354485
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:18:57.814802
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    # Type checks
    result = Right(1).to_lazy()
    assert isinstance(result, Either)
    assert isinstance(result.value, Callable)


# Generated at 2022-06-14 03:18:59.177845
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    value = 2
    assert Either(value).to_lazy().force() == value


# Generated at 2022-06-14 03:19:01.829718
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monoid import Sum

    assert(Lazy(lambda: Sum(1)) == Right(Sum(1)).to_lazy())

# Generated at 2022-06-14 03:19:06.521753
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Right(2).to_lazy()
    assert Lazy(lambda: 2) == Left(2).to_lazy()



# Generated at 2022-06-14 03:19:15.130591
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right('success').to_lazy() == Lazy(lambda: 'success')



# Generated at 2022-06-14 03:19:19.547342
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(123).to_lazy() == Lazy(lambda: 123)
    assert Right(123).to_lazy() == Lazy(lambda: 123)


# Generated at 2022-06-14 03:19:22.052320
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('test').to_lazy() == Lazy(lambda: 'test')
    assert Right('test2').to_lazy() == Lazy(lambda: 'test2')



# Generated at 2022-06-14 03:19:28.760326
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    @Lazy
    def should_be_lazy():
        return True

    assert Right(True).to_lazy() == should_be_lazy
    assert Left(True).to_lazy() == should_be_lazy

# Generated at 2022-06-14 03:19:30.972014
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:19:33.415514
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Either(1).to_lazy()
    assert isinstance(Either(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:19:37.903698
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    left_either = Left("Error")
    right_either = Right("Value")

    assert left_either.to_lazy() == Lazy(lambda: "Error")
    assert right_either.to_lazy() == Lazy(lambda: "Value")


# Generated at 2022-06-14 03:19:42.846727
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    x = Left(2).to_lazy()  # Lazy monad with value 2
    y = Right(3).to_lazy()  # Lazy monad with value 3



# Generated at 2022-06-14 03:19:55.705121
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    lazy_instance = Lazy(lambda: "lazy value")
    assert Right("Right value").to_lazy() == lazy_instance
    assert Left("Left value").to_lazy() == lazy_instance



# Generated at 2022-06-14 03:20:00.917730
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def lazy_sum(x, y):
        return x + y

    assert Right(1).to_lazy().bind(lazy_sum, 4) == 5
    assert Left(1).to_lazy().bind(lazy_sum, 2) == 3

# Generated at 2022-06-14 03:20:12.864104
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    value = 4

    r = Right(value)

    assert r.to_lazy().force() == value

    l = Left(value)

    assert l.to_lazy().force() == value

# Generated at 2022-06-14 03:20:17.749191
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right = Either(1)
    left = Either(2)

    assert right.to_lazy().value() == 1
    assert left.to_lazy().value() == 2


# Generated at 2022-06-14 03:20:22.677987
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(7).to_lazy() == Lazy(lambda: 7)
    assert Right(8).to_lazy() == Lazy(lambda: 8)


# Generated at 2022-06-14 03:20:28.402029
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy().force() == 5
    assert Left(5).to_lazy().force() == 5


# Generated at 2022-06-14 03:20:31.453220
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def fun():
        return 'fun'

    assert Left('err').to_lazy() == Lazy(lambda: 'err')
    assert Right('success').to_lazy() == Lazy(lambda: 'success')


# Generated at 2022-06-14 03:20:33.331192
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(1).to_lazy(), Lazy)



# Generated at 2022-06-14 03:20:37.068161
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left('error')
    assert left.to_lazy() == Lazy(lambda: 'error')

    right = Right('success')
    assert right.to_lazy() == Lazy(lambda: 'success')



# Generated at 2022-06-14 03:20:43.145291
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Tests for method to_lazy of class Either
    """
    from pymonet.lazy import Lazy

    assert Left("error").to_lazy() == Lazy(lambda: "error")
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:20:46.773727
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    import pytest

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right(4).to_lazy() == Lazy(lambda: 4)



# Generated at 2022-06-14 03:20:51.276283
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def _():
        pass

    assert Right(1).to_lazy() == Lazy(_)
    assert Right(1).to_lazy() == Lazy(_)



# Generated at 2022-06-14 03:20:53.649276
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def f():
        return 1
    assert Right(1).to_lazy()._function == f


# Generated at 2022-06-14 03:21:00.269697
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    from pymonet.either import Right, Left

    lazy_value = Right("Blop").to_lazy()

    assert type(lazy_value) is Lazy
    assert lazy_value.evaluate() == "Blop"

    lazy_value = Left("Blop").to_lazy()

    assert type(lazy_value) is Lazy
    assert lazy_value.evaluate() == "Blop"


# Generated at 2022-06-14 03:21:01.812054
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert (Left('error').to_lazy().force() == 'error')
    assert (Right(1).to_lazy().force() == 1)

# Generated at 2022-06-14 03:21:15.054317
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:16.522782
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(lambda x: x + 2).to_lazy() == Lazy(lambda: lambda x: x + 2)

# Generated at 2022-06-14 03:21:18.602128
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert(Lazy(lambda: 2) == Right(2).to_lazy())
    assert(Lazy(lambda: 'Some text') == Right('Some text').to_lazy())


# Generated at 2022-06-14 03:21:22.969444
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:27.907572
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def return_one():
        return 1

    assert Right(1).to_lazy() == Lazy(return_one)
    assert Left(1).to_lazy() == Lazy(return_one)



# Generated at 2022-06-14 03:21:31.287869
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_value = lambda: 'lazy-value'

    assert Lazy(lazy_value) == Right('value').to_lazy() == Left('value').to_lazy()



# Generated at 2022-06-14 03:21:32.667070
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().is_instance_of(Lazy)

# Generated at 2022-06-14 03:21:35.757998
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:38.090867
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy, Thunk

    assert Right(4).to_lazy() == Lazy(Thunk(4))



# Generated at 2022-06-14 03:21:42.055229
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:22:05.197558
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Lazy)


# Test for method case of class Either

# Generated at 2022-06-14 03:22:09.141037
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Left(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:22:11.073243
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left('a').to_lazy() == Lazy(lambda: 'a')
    assert Right('a').to_lazy() == Lazy(lambda: 'a')


# Generated at 2022-06-14 03:22:19.060374
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from funcs import add
    import pytest
    def add1(x: int) -> int:
        return x + 1
    e = Right(add)
    assert e.to_lazy() == Lazy(add)
    assert e.to_lazy().value() == add
    assert e.to_lazy().map(add1).value()(1) == 3

    e = Left(add)
    assert e.to_lazy() == Lazy(add)
    assert e.to_lazy().value() == add
    with pytest.raises(Exception) as execinfo:
        _ = e.to_lazy().map(add1).value()
    assert 'add' in str(execinfo.value)


# Generated at 2022-06-14 03:22:23.677281
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def f(x):
        return x

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:22:29.504204
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    right_value = "right_value"
    right_either = Right(right_value)
    lazy_right = right_either.to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.value() == right_value

    left_value = "left_value"
    left_either = Left(left_value)
    lazy_left = left_either.to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.value() == left_value

# Generated at 2022-06-14 03:22:35.521045
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Either(2).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy() == 2

    lazy = Either('test').to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy() == 'test'



# Generated at 2022-06-14 03:22:38.851592
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Either(1).to_lazy()
    assert Lazy(lambda: 'test') == Either('test').to_lazy()



# Generated at 2022-06-14 03:22:41.483745
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:22:52.408289
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    from pymonet.lazy import Lazy

    assert Either.is_left(Left(4).to_lazy()) is True
    assert Either.is_right(Left(4).to_lazy()) is False
    assert Left(4).to_lazy().value() is None
    assert Either.is_left(Right(4).to_lazy()) is False
    assert Either.is_right(Right(4).to_lazy()) is True
    assert Right(4).to_lazy().value() == 4

    with pytest.raises(TypeError):
        Left(4).to_lazy().bind(lambda x: Lazy(lambda x: x ** 2))


# Generated at 2022-06-14 03:23:39.065882
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.
    """
    from pymonet.lazy import Lazy

    def func() -> bool:
        return False

    assert Lazy(func) == Right(False).to_lazy()

# Generated at 2022-06-14 03:23:42.591055
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Left(1)).run() == 1
    assert Either.to_lazy(Right(2)).run() == 2



# Generated at 2022-06-14 03:23:56.862586
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from random import randint

    random_number = randint(0, 1000)

    result_either = Either(random_number).to_lazy()

    assert isinstance(result_either, Lazy)
    assert result_either.value() == random_number

# Generated at 2022-06-14 03:24:00.374255
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().get() == 1
    assert Right(2).to_lazy().get() == 2

# Generated at 2022-06-14 03:24:03.077616
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:24:05.719440
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Right(1)) == Lazy(lambda: 1)
    assert Either.to_lazy(Left(1)) == Lazy(lambda: 1)

# Generated at 2022-06-14 03:24:08.205078
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def value(): return 2 + 2

    assert Either.to_lazy(Right(4)) == Lazy(value)
    assert Either.to_lazy(Left(4)) == Lazy(None)



# Generated at 2022-06-14 03:24:13.344972
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Either(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Either(Box(1)).to_lazy().force() == Box(1)



# Generated at 2022-06-14 03:24:16.418157
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either
    """
    expect = "Test"
    lazy = Either("Test").to_lazy()
    actual = lazy.value()
    assert actual == expect

# Generated at 2022-06-14 03:24:19.664784
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:25:57.160583
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Either(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:26:00.716754
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.Right(lambda x: x + 3).to_lazy() == Lazy(lambda: lambda x: x + 3)
    assert Either.Left(lambda x: x + 3).to_lazy() == Lazy(lambda: lambda x: x + 3)

# Generated at 2022-06-14 03:26:03.437402
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Left("Error!").to_lazy() == Lazy(lambda: "Error!")



# Generated at 2022-06-14 03:26:05.624671
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Left('test')) == Lazy(lambda: 'test')
    assert Either.to_lazy(Right('test')) == Lazy(lambda: 'test')



# Generated at 2022-06-14 03:26:07.780200
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def foo():
        return 3
    success = Right(5)

    assert success.to_lazy() == Lazy(foo)

# Generated at 2022-06-14 03:26:16.718957
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.either import Right, Left
    from pymonet.maybe import Maybe

    def test_right():
        right = Right(1)

        assert right.to_lazy() == Lazy(lambda: 1)
        assert right.to_box() == Box(1)
        assert right.to_try() == Try(1)
        assert right.to_maybe() == Maybe.just(1)

    def test_left():
        left = Left("test")

        assert left.to_lazy() == Lazy(lambda: "test")
        assert left.to_box() == Box("test")

# Generated at 2022-06-14 03:26:22.992577
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    func = lambda: "func"
    value_valid = "value"
    value_invalid = None
    either_valid = Right(value_valid)
    either_invalid = Left(value_invalid)

    assert either_valid.to_lazy().value() == value_valid
    assert either_invalid.to_lazy().value() == value_invalid
    assert either_valid.to_lazy().apply(func) == func()
    assert either_invalid.to_lazy().apply(func) == value_invalid



# Generated at 2022-06-14 03:26:28.424142
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:26:35.518090
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.validation import Validation

    # Create Lazy value
    lazy_value = 42
    lazy = Lazy(lambda: lazy_value)

    # Create Box value
    box_value = 42
    box = Box(box_value)

    # Create Validation value
    validation_value = 42
    validation = Validation.success(validation_value)

    # Check value type
    assert lazy.to_lazy() == lazy
    assert box.to_lazy() == lazy
    assert validation.to_lazy() == lazy


# Generated at 2022-06-14 03:26:38.150994
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy

    def test_function():
        return "value"

    assert Right("value").to_lazy() == Lazy(test_function)
