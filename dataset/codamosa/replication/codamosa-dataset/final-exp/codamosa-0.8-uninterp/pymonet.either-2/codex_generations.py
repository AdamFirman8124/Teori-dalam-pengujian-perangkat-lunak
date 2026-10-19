

# Generated at 2022-06-14 03:16:45.342058
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1).__eq__(Left(1)) == True
    assert Left(1).__eq__(Right(1)) == False
    assert Right(1).__eq__(Right(1)) == True
    assert Right(1).__eq__(Left(1)) == False
    assert Right(1).__eq__(Left(2)) == False


# Generated at 2022-06-14 03:16:55.145879
# Unit test for method case of class Either
def test_Either_case():
    # Arrange
    left = Left(5)
    right = Right(5)

    # Act
    left_result = left.case(error=lambda x: x, success=lambda x: x + 3)
    right_result = right.case(error=lambda x: x, success=lambda x: x + 3)

    # Assert
    assert 5 == left_result
    assert 8 == right_result


# Generated at 2022-06-14 03:16:58.732451
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Either(2).__eq__(Either(2))
    # not isinstance(Either(2), type(Right))
    assert not Either(2).__eq__(Right(2))
    assert not Either(2).__eq__(Right(3))


# Generated at 2022-06-14 03:17:00.162996
# Unit test for method __eq__ of class Either
def test_Either___eq__():

    left = Left(None)
    another_left = Left(None)
    right = Right(None)

    assert left == another_left
    assert not left == right

# Generated at 2022-06-14 03:17:03.854973
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy function of Either monad.
    """
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either("1").to_lazy() == Lazy(lambda: "1")


# Generated at 2022-06-14 03:17:11.539732
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Either.right(2).to_lazy()
    assert right == Lazy(lambda: 2)

    left = Either.left("xxx").to_lazy()
    assert left == Lazy(lambda: "xxx")


# Generated at 2022-06-14 03:17:13.670646
# Unit test for method case of class Either
def test_Either_case():
    def double(x):
        return x * 2

    def square(x):
        return x**2

    assert Right(2).case(double, square) == 4
    assert Left(2).case(double, square) == 4


# Generated at 2022-06-14 03:17:21.191058
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(9) != Right(8)
    assert Right(8) != Right(8)
    assert Left(9) != Left(8)
    assert Left(8) != Left(8)
    assert Right(8) != Left(8)
    assert Left(8) != Right(8)



# Generated at 2022-06-14 03:17:29.637478
# Unit test for method case of class Either
def test_Either_case():
    """
    >>> b = Left(1)
    >>> b.case(error=lambda x: x + 1, success=lambda x: x)
    2
    >>> b = Right(2)
    >>> b.case(error=lambda x: x + 1, success=lambda x: x)
    2
    """



# Generated at 2022-06-14 03:17:34.055227
# Unit test for method case of class Either
def test_Either_case():
    assert Left(1).case(lambda x: x + 3, lambda x: x + 8) == 4
    assert Right(3).case(lambda x: x + 3, lambda x: x + 8) == 11


# Generated at 2022-06-14 03:17:39.850081
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(4).to_lazy() == Lazy(lambda: 4)
    assert Right(4).to_lazy() == Lazy(lambda: 4)


# Generated at 2022-06-14 03:17:45.542830
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Try(1, is_success=True).to_lazy() == Lazy(lambda: 1)
    assert Try(1, is_success=False).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:17:47.677550
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def foo() -> int:
        return 2
    assert Right(foo) == Right(foo).to_lazy().eval()


# Generated at 2022-06-14 03:17:48.937614
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(5).to_lazy().evaluate() == 5


# Generated at 2022-06-14 03:17:53.150876
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    right = Right(1)
    left = Left(1)
    # When
    right_lazy = right.to_lazy()
    left_lazy = left.to_lazy()
    # Then
    assert right_lazy.eval() == 1
    assert left_lazy.eval() == 1



# Generated at 2022-06-14 03:17:55.493919
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:18:08.340504
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for :func: '~Either.to_lazy' of class Either
    """
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert not Lazy(lambda: 5) == Lazy(lambda: 5)
    assert not Left([1, 2, 3]).to_lazy() == Left([1, 2, 3]).to_lazy()
    assert not Left('test').to_lazy() == Left('test').to_lazy()
    assert not Right('test').to_lazy() == Right('test').to_lazy()
    assert not Left('test').to_lazy() == Right('test').to_lazy()

# Generated at 2022-06-14 03:18:13.236949
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()


# Generated at 2022-06-14 03:18:20.838380
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(10).to_lazy() == Lazy(lambda: 10) and\
            Left('').to_lazy() == Lazy(lambda: '') and\
            Left([]).to_lazy() == Lazy(lambda: []) and\
            Left({}).to_lazy() == Lazy(lambda: {}) and\
            Left(()).to_lazy() == Lazy(lambda: ())

# Generated at 2022-06-14 03:18:23.990806
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_of_right = Either(lambda x: x + 5).to_lazy()
    assert lazy_of_right.evaluate(10) == 15



# Generated at 2022-06-14 03:18:29.310625
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:18:35.679213
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Either(5).to_lazy()
    assert Right(5).to_lazy() == Either(5).to_lazy()


# Generated at 2022-06-14 03:18:38.293834
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(None).to_lazy() == Lazy(lambda: None)
    assert Right(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:18:40.379849
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(5).to_lazy().eval() == 5
    assert Right(5).to_lazy().eval() == 5


# Generated at 2022-06-14 03:18:45.213533
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    is_right = Either(3).to_lazy().value() == Either(3)
    is_left = Either.left(-3).to_lazy().value() == Either.left(-3)

    assert is_right and is_left



# Generated at 2022-06-14 03:18:47.603951
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    val = Either(10)
    assert isinstance(val, Either)
    assert isinstance(val.to_lazy(), Lazy)
    assert val.to_lazy().lazy_eval() is 10

# Generated at 2022-06-14 03:18:51.034150
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:18:58.665290
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for Either to_lazy method.

    :returns: Nothing
    :rtype: None
    """
    import unittest

    class ToLazyTest(unittest.TestCase):
        """
        Unit test for Either to_lazy method.
        """

        def test_to_lazy(self):
            """
            Test for Either to_lazy method.

            :returns: Nothing
            :rtype: None
            """
            from pymonet.lazy import Lazy

            self.assertEqual(Right(3).to_lazy(), Lazy(lambda: 3))
            self.assertEqual(Left(7).to_lazy(), Lazy(lambda: 7))

    unittest.main()


# Generated at 2022-06-14 03:19:02.003179
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    either = Right(3).to_lazy()

    assert either.is_instance(Right)
    assert either.value() == 3

    either = Left(8).to_lazy()

    assert either.is_instance(Left)
    assert either.value() == 8


# Generated at 2022-06-14 03:19:09.168675
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    value = 1
    # Create new Right with value
    either = Right(value)
    # Create lazy function returning value
    lazy = Lazy(lambda: value)
    # Transform Either to lazy
    result = either.to_lazy()
    # Check if values are equal
    assert result == lazy
    # Get mapped value
    result = result.get()
    # Check if mapped value is equal previous value
    assert result == value


# Generated at 2022-06-14 03:19:20.878114
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN
    right = Either.right(123)
    left = Either.left(None)

    # THEN
    assert right.to_lazy().eval() == 123
    assert left.to_lazy().eval() == None


# Generated at 2022-06-14 03:19:26.512405
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either
    """
    from pymonet.lazy import Lazy
    from pymonet.either import Either
    from pymonet.either import Right, Left

    assert isinstance(Either.to_lazy(Right(3)), Lazy)
    assert isinstance(Either.to_lazy(Left(3)), Lazy)



# Generated at 2022-06-14 03:19:32.769587
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import value

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert value(Left(5).to_lazy()) == 5
    assert value(Right(5).to_lazy()) == 5


# Generated at 2022-06-14 03:19:36.704149
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Right(None)) == Either.to_lazy(Left(None)) == Lazy(lambda: None)


# Generated at 2022-06-14 03:19:42.006405
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'text') == Left('text').to_lazy()
    assert Lazy(lambda: 'text') == Right('text').to_lazy()


# Generated at 2022-06-14 03:19:46.081299
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN
    either = Left('I Am Not Right')

    # WHEN
    result = either.to_lazy()

    # THEN
    assert isinstance(result, Lazy)
    assert result.get() == either.value

# Generated at 2022-06-14 03:19:48.829264
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:19:52.273105
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(2).to_lazy() == Right(2).to_lazy()



# Generated at 2022-06-14 03:20:02.649341
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    # When Either is Left
    left = Left(Try(Exception))

    # Then it must be transformed to Lazy returning same value but wrapped in Try
    assert left.to_lazy() == Lazy(lambda: Try(Exception))

    # When Either is Right
    right = Right(Try(ValueError))

    # Then it must be transformed to Lazy returning same value but wrapped in Try
    assert right.to_lazy() == Lazy(lambda: Try(ValueError))



# Generated at 2022-06-14 03:20:04.425481
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left[int](5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:20:34.588374
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Either('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Left('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Right('foo').to_lazy() == Lazy(lambda: 'foo')


# Generated at 2022-06-14 03:20:39.897146
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def fn(x):
        return x
    assert Right(3).to_lazy() == Lazy(fn)(3), "to_lazy should return Lazy with value 3"
    assert Left(3).to_lazy() == Lazy(fn)(3), "to_lazy should return Lazy with value 3"


# Generated at 2022-06-14 03:20:43.663861
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:20:47.345335
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left(1)
    assert left.to_lazy() == Lazy(lambda: 1)
    right = Right(2)
    assert right.to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:20:52.697223
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:20:57.263496
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(1).to_lazy().value(), int)
    assert Right(1).to_lazy().value() == 1
    assert isinstance(Left(1).to_lazy().value(), type(None))
    assert Left(1).to_lazy().value() is None

# Generated at 2022-06-14 03:20:59.796416
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_either = Lazy(lambda: Right(3)).to_lazy()

    a_lazy = lazy_either.map(lambda x: x + 1)

    b_lazy = lazy_either.map(lambda x: x + 1)

    assert a_lazy == b_lazy
    assert a_lazy.get() == 4


# Generated at 2022-06-14 03:21:08.564968
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def add_one(num):
        return num + 1

    # Test with Right
    either = Right(2)
    lazy = either.to_lazy()
    assert lazy.value == 2
    assert lazy.force() == 2
    assert lazy.map(add_one) == Right(3)
    assert lazy.map(add_one).force() == 3
    assert lazy.ap(Right(add_one)) == Right(add_one(2))
    assert lazy.ap(Right(add_one)).force() == 3
    assert lazy.bind(add_one).force() == 3

    # Test with Left
    either = Left('error')
    lazy = either.to_lazy()
    assert lazy.value == 'error'
    assert lazy.force() == 'error'

# Generated at 2022-06-14 03:21:13.022429
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Either.Right(4).to_lazy() == Lazy(lambda: 4)
    assert Either.Right(Box(4)).to_lazy() == Lazy(lambda: Box(4))
    assert Either.left(4).to_lazy() == Lazy(lambda: 4)

# Generated at 2022-06-14 03:21:15.126500
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Lazy)

# Generated at 2022-06-14 03:21:48.363948
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().is_lazy()
    assert Either(2).to_lazy().eval() == 2
    assert Either("3").to_lazy().eval() == "3"
    assert Either([4]).to_lazy().eval() == [4]
    assert Either(5).to_lazy().eval() == 5.0


# Generated at 2022-06-14 03:21:53.911045
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either('Some string').to_lazy() == Lazy(lambda: 'Some string')


# Generated at 2022-06-14 03:21:56.223249
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().get() == 1



# Generated at 2022-06-14 03:22:00.095219
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:22:03.324433
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:22:06.844244
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    value = 5
    assert isinstance(Right(value).to_lazy(), Lazy)
    assert Lazy(lambda: value) == Right(value).to_lazy()



# Generated at 2022-06-14 03:22:15.390921
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Ensure Either.to_lazy returns Lazy with function returning previous value.

    :returns: always true
    :rtype: Boolean
    """
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either("test").to_lazy() == Lazy(lambda: "test")
    assert Either(Box("test")).to_lazy() == Lazy(lambda: Box("test"))
    assert Either(Try("test")).to_lazy() == Lazy(lambda: Try("test"))
    return True


# Generated at 2022-06-14 03:22:18.166904
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # test for Either.Left
    assert Either.Left('error').to_lazy().get() == 'error'
    # test for Either.Right
    assert Either.Right('success').to_lazy().get() == 'success'

# Generated at 2022-06-14 03:22:22.349507
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'value') == Either('value').to_lazy()



# Generated at 2022-06-14 03:22:25.694572
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy().value() == 5
    assert Left(5).to_lazy().value() == 5



# Generated at 2022-06-14 03:23:35.510651
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:23:39.773372
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Left(1).to_lazy() == Right(1).to_lazy()


# Generated at 2022-06-14 03:23:50.431750
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.functions import add2, multiply2, divide2, subtract2
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Left(Box(5)).to_lazy() == Lazy(lambda: Box(5))
    assert Right(Box(5)).to_lazy() == Lazy(lambda: Box(5))

    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)

    assert Left("PyMonet").to_lazy() == Lazy(lambda: "PyMonet")
    assert Right("PyMonet").to_lazy() == Lazy(lambda: "PyMonet")


# Generated at 2022-06-14 03:23:56.227362
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test for method to_lazy of class Either.
    """
    assert Left('left').to_lazy().force() == 'left'
    assert Right('right').to_lazy().force() == 'right'



# Generated at 2022-06-14 03:24:00.811338
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    left = Left(2)
    assert left.to_lazy().value() == 2

    right = Right(2)
    assert right.to_lazy().value() == 2


# Generated at 2022-06-14 03:24:02.640727
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(3).to_lazy().get() == 3
    assert Left(3).to_lazy().get()  == 3


# Generated at 2022-06-14 03:24:04.335337
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Either('foo').case(Left, Right).to_lazy() == Lazy(lambda: 'foo')

# Generated at 2022-06-14 03:24:06.245163
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Either.to_lazy(Either.from_value(5))
    assert lazy == Lazy(lambda: 5)


# Generated at 2022-06-14 03:24:17.074314
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Nothing
    from pymonet.box import Box

    # left <<< ! <<< empty
    result = Lazy.unit(Nothing()).bind(lambda x: x.value.to_lazy())
    assert result == Left(None).to_lazy()
    # left <<< ! <<< nothing
    result = Lazy.unit(Box(Nothing())).bind(lambda x: x.value.value.to_lazy())
    assert result == Left(None).to_lazy()
    # left <<< ! <<< just
    result = Lazy.unit(Box(Nothing())).bind(lambda x: x.value.value.to_lazy())
    assert result == Left(None).to_lazy()
    # right <<< ! <<< just

# Generated at 2022-06-14 03:24:19.967048
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left('error').to_lazy() == Lazy(lambda: 'error')