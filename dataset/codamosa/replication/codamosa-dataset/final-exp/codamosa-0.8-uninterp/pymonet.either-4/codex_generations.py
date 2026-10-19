

# Generated at 2022-06-14 03:16:48.327791
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1).__eq__(Right(1))
    assert Left(1).__eq__(Left(1))
    assert Left(1).__eq__(Right(1)) == False
    assert Right(1).__eq__(Left(1)) == False
    assert Left(1).__eq__(Left(2)) == False
    assert Right(1).__eq__(Right(2)) == False


# Generated at 2022-06-14 03:16:52.728010
# Unit test for method case of class Either
def test_Either_case():
    assert Left(2).case(
        error=lambda x: x + 2,
        success=lambda x: x + 1
    ) == 4
    assert Right(1).case(
        error=lambda x: x + 2,
        success=lambda x: x + 1
    ) == 2

# Generated at 2022-06-14 03:16:56.965397
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert(Left(1) == Left(1))
    assert(Right(1) == Right(1))
    assert(Left(1) != Left(2))
    assert(Right(1) != Right(2))
    assert(Left(1) != Right(1))
    assert(Right(1) != Left(1))

# Generated at 2022-06-14 03:17:14.895586
# Unit test for method case of class Either
def test_Either_case():
    assert Left(10).case(lambda error: error, lambda success: success) == 10
    assert Left(10).case(lambda error: error + 1, lambda success: success) == 10
    assert Left(10).case(lambda error: error - 1, lambda success: success) == 9
    assert Right(10).case(lambda error: error, lambda success: success) == 10
    assert Right(10).case(lambda error: error + 1, lambda success: success) == 10
    assert Right(10).case(lambda error: error - 1, lambda success: success) == 10

# Generated at 2022-06-14 03:17:19.809523
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left1 = Left(1)
    left2 = Left(1)
    right = Right(1)

    assert left1 == left2
    assert left1 != right
    assert right != left1

# Generated at 2022-06-14 03:17:22.968398
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right('a') != Right('b')
    assert Left('a') != Left('b')
    assert Right(1) != Left(1)
    assert Left(1) != Right(1)


# Generated at 2022-06-14 03:17:28.336805
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:17:32.112282
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Left(1) != Right(1)


# Generated at 2022-06-14 03:17:34.472716
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    result = Left(1).to_lazy()

    assert result == Lazy(lambda: 1), "Method to_lazy of class Either return Lazy with value which is stored in Either"



# Generated at 2022-06-14 03:17:37.749218
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:17:45.984057
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Left('error').to_lazy(), Lazy)
    assert isinstance(Right('success').to_lazy(), Lazy)
    assert Left('error').to_lazy() == Right('success').to_lazy()
    assert not Left('error').to_lazy() == Right('failure').to_lazy()



# Generated at 2022-06-14 03:17:47.898141
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().value() == 1
    assert Left(None).to_lazy().value() is None



# Generated at 2022-06-14 03:17:52.186319
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.box import Box

    assert Either.to_lazy(Left(2)) == Lazy(Box(2))
    assert Either.to_lazy(Right(3)) == Lazy(Box(3))


# Generated at 2022-06-14 03:17:57.941438
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(Lazy(lambda: 2)).to_lazy() == Lazy(lambda: 2)
    assert Either(Lazy(lambda: 3)).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:18:01.636152
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:18:05.848190
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(12).to_lazy() == Lazy(lambda: 12)
    assert Right(14).to_lazy() == Lazy(lambda: 14)



# Generated at 2022-06-14 03:18:11.196525
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_maybe import Maybe
    from pymonet.lazy import Lazy

    x = Either.left(1)
    y = Either.right(1)

    assert x.to_lazy() == Lazy(lambda: x)
    assert y.to_lazy() == Lazy(lambda: y)



# Generated at 2022-06-14 03:18:15.621170
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    result = Right(2).to_lazy()
    assert result.value() == 2
    assert result.value() == 2
    result = Left(2).to_lazy()
    assert result.value() == 2
    assert result.value() == 2

# Generated at 2022-06-14 03:18:16.858111
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Left(5)) == Left(5).to_lazy()


# Generated at 2022-06-14 03:18:19.947699
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    >>> Either.to_lazy = test_Either_to_lazy
    >>> Right(42).to_lazy().run()
    42
    >>> Left('Something wrong').to_lazy().run()
    'Something wrong'
    """
    from pymonet.lazy import Lazy
    return Lazy(lambda: self.value)

# Generated at 2022-06-14 03:18:26.029172
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test Either.to_lazy method.

    :returns: None
    :rtype: None
    """
    assert Left(1).to_lazy().get() == 1
    assert Right(1).to_lazy().get() == 1


# Generated at 2022-06-14 03:18:29.429433
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert(Lazy(lambda: 1) == Either(1).to_lazy())
    assert(Lazy(lambda: 2) == Either(2).to_lazy())



# Generated at 2022-06-14 03:18:34.290226
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right = Right(5)
    assert right.to_lazy().value() == 5

    left = Left(5)
    assert left.to_lazy().value() == 5



# Generated at 2022-06-14 03:18:38.741376
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    value = 10
    either = Left(value)
    lazy = either.to_lazy()

    assert lazy == Lazy(lambda: value) and lazy.is_forced == False


# Generated at 2022-06-14 03:18:40.785961
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:18:46.384949
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left('2').to_lazy() == Lazy(Left('2').value)
    assert Right('2').to_lazy() == Lazy(Right('2').value)


# Generated at 2022-06-14 03:18:50.474763
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    value = Right(1)
    lazy = value.to_lazy()
    assert lazy.__class__.__name__ == 'Lazy'
    assert lazy.value() == 1

# Generated at 2022-06-14 03:19:01.102006
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:19:05.369405
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert(Left(10).to_lazy().value() == 10)
    assert(Right(10).to_lazy().value() == 10)


# Generated at 2022-06-14 03:19:09.733477
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    # Arrange
    box = Box(5)
    lazy = Lazy(lambda: 5)

    # Act
    result = box.to_lazy()

    # Assert
    assert lazy == result


# Generated at 2022-06-14 03:19:19.537572
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test transforming Either to Lazy.

    :returns: True when tests pass
    :rtype: Boolean
    """
    from pymonet.lazy import Lazy

    assert Right(12).to_lazy() == Lazy(lambda: 12)
    assert Left(12).to_lazy() == Lazy(lambda: 12)
    print('Either to lazy test: pass')
    return True



# Generated at 2022-06-14 03:19:25.227046
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_either import Either
    from pymonet.lazy import Lazy

    assert Either(2).to_lazy() == Lazy(lambda: 2)
    assert Maybe(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:19:36.855430
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def something():
        return 1

    assert Left(1).to_lazy().value() == something()
    assert Right(1).to_lazy().value() == something()


# Generated at 2022-06-14 03:19:43.319125
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert (Try(5, is_success=False)).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:19:44.873045
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    assert Either(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:19:48.282732
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert (Right(1).to_lazy()) == Lazy(lambda: 1)
    assert (Left(1).to_lazy()) == Lazy(lambda: 1)

# Generated at 2022-06-14 03:19:50.761411
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    a = Either.right(10)
    assert(a.to_lazy() == Lazy(lambda: 10))


# Generated at 2022-06-14 03:19:55.251129
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().get() == 1
    assert Left([42, 'error!']).to_lazy().get() == [42, 'error!']

# Generated at 2022-06-14 03:20:00.708592
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:20:13.596891
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left("error").to_lazy() == Lazy(lambda: "error")


# Generated at 2022-06-14 03:20:23.837572
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    test_object = Right(1)
    expected_object = Lazy(lambda: 1)

    actual_object = test_object.to_lazy()

    assert expected_object == actual_object


# Generated at 2022-06-14 03:20:25.097895
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Right(1)) == Lazy(lambda: 1)



# Generated at 2022-06-14 03:20:34.246400
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.box import Box
    from pymonet.monad_try import Try

    assert Left('e').to_lazy() == Lazy(lambda: 'e')
    assert Left(None).to_lazy() == Lazy(lambda: None)
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Left(0).to_lazy() == Lazy(lambda: 0)
    assert Left(1.1).to_lazy() == Lazy(lambda: 1.1)
    assert Left({1: 'a'}).to_lazy() == Lazy(lambda: {1: 'a'})

# Generated at 2022-06-14 03:20:36.267449
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1



# Generated at 2022-06-14 03:20:39.348419
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(1).to_lazy().evaluate() == 1
    assert Left(2).to_lazy().evaluate() == 2

# Generated at 2022-06-14 03:20:44.532832
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:20:48.442507
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy method of Either
    """
    value = 1

    assert Right(value).to_lazy() == Left(value).to_lazy()
    assert Left(value).to_lazy().value() == value
    assert Right(value).to_lazy().value() == value


# Generated at 2022-06-14 03:20:52.901975
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def three() -> int:
        return 3

    assert Right(3).to_lazy() == Lazy(three)
    assert Left(3).to_lazy() == Lazy(three)


# Generated at 2022-06-14 03:20:56.425971
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Right(2).to_lazy()
    assert Lazy(lambda: 2) == Left(2).to_lazy()


# Generated at 2022-06-14 03:20:59.806869
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Either(1).to_lazy() == Lazy(1)
    assert Either(2).to_lazy() == Lazy(2)


# Generated at 2022-06-14 03:21:18.858830
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def test_unit():
        return 1

    assert Right(1).to_lazy() == Lazy(test_unit)
    assert Left(1).to_lazy() == Lazy(test_unit)


# Generated at 2022-06-14 03:21:20.495356
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(5).to_lazy() == Right(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:21:22.400621
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    val = Right(1)
    lazy = val.to_lazy()
    assert lazy.get() == 1



# Generated at 2022-06-14 03:21:25.943805
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(0).to_lazy() == Lazy(lambda: 0)
    assert Right(4).to_lazy() == Lazy(lambda: 4)


# Generated at 2022-06-14 03:21:27.445469
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left('Expected error').to_lazy() == Lazy(lambda: 'Expected error')


# Generated at 2022-06-14 03:21:33.151531
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Test to_lazy method of class Either"""
    from pymonet.lazy import Lazy

    test_value = 7
    either = Right(test_value)
    assert Lazy(lambda: test_value) == either.to_lazy()

    test_value = 'test'
    either = Left(test_value)
    assert Lazy(lambda: test_value) == either.to_lazy()



# Generated at 2022-06-14 03:21:37.231124
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    either: Either[int] = Left(0)
    lazy_left_either = either.to_lazy() # Type: Lazy[int]
    assert lazy_left_either() == 0

    either = Right(0)
    lazy_right_either = either.to_lazy()
    assert lazy_right_either() == 0

# Generated at 2022-06-14 03:21:42.014179
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 1)
    left_either = Left(1)
    right_either = Right(1)

    assert lazy == left_either.to_lazy()
    assert lazy == right_either.to_lazy()



# Generated at 2022-06-14 03:21:44.212042
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right('right').to_lazy() == Lazy(lambda: 'right')


# Generated at 2022-06-14 03:21:50.957891
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(5).to_lazy(), Lazy)

    def _test() -> int:
        return 1
    assert Right(5).to_lazy().value() == 5
    assert Left(_test()).to_lazy().value() == 1



# Generated at 2022-06-14 03:22:31.181464
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Either(Try.success('foo')).to_lazy() == Lazy(lambda: Try.success('foo'))
    assert Either(Try.fail('foo')).to_lazy() == Lazy(lambda: Try.fail('foo'))


# Generated at 2022-06-14 03:22:32.876088
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:22:34.446406
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(10).to_lazy().call() == 10
    assert Left(10).to_lazy().call() == 10


# Generated at 2022-06-14 03:22:38.279337
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    def get19():
        return 19
    right = Right(19)
    lazy = right.to_lazy()
    assert(lazy.value() == 19)
    assert(lazy == Lazy(get19))


# Generated at 2022-06-14 03:22:41.786745
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Left(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:22:44.718826
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:22:54.874312
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from unittest import TestCase
    from pymonet.lazy import Lazy
    from pymonet.either import Either
    from pymonet.either import Right
    from pymonet.either import Left

    class EitherToLazyTests(TestCase):
        def test_to_lazy_right(self):
            value = "Success"
            e = Right(value)
            result = e.to_lazy()

            assert isinstance(result, Lazy)
            assert result.eval() == value

        def test_to_lazy_left(self):
            value = "Fail"
            e = Left(value)
            result = e.to_lazy()

            assert isinstance(result, Lazy)
            assert result.eval() == value

    EitherToLazyTests().test_to_lazy_

# Generated at 2022-06-14 03:23:08.999412
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation
    from pymonet.box import Box
    from pymonet.either import Right, Left
    from pymonet.maybe import Maybe

    right: Either[int] = Right(2)
    lazy = right.to_lazy()
    # the result of the execution of the lazy monad must return the value of the right monad
    assert lazy.execute() == 2 
    # the monad lazy must have the same value as the monad right
    assert lazy.value == 2
    # the monad lazy has the function to get the value
    assert lazy.function() == 2
    assert lazy.function is not None

    left: Either[int] = Left(1)
    lazy = left

# Generated at 2022-06-14 03:23:11.358054
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    assert Right(1).to_lazy()(lambda: 2) == 1

# Generated at 2022-06-14 03:23:13.643313
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(10).to_lazy() != Lazy(lambda: 10)
    assert Left(10).to_lazy() != Lazy(lambda: 10)


# Generated at 2022-06-14 03:23:50.491116
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Specification test for method to_lazy of class Either
    """
    right = Right(42)
    assert right.to_lazy()().value == 42

# Generated at 2022-06-14 03:24:03.369259
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    def to_lazy_spec(f: Callable[[Any], Any], v: Any, expect: Any):
        result = f(v)
        assert isinstance(result, Lazy)
        assert result.value() == expect

    to_lazy_spec(lambda x: Right(x).to_lazy(), 5, 5)
    to_lazy_spec(lambda x: Right(x).to_lazy(), 'a', 'a')
    to_lazy_spec(lambda x: Left(x).to_lazy(), 5, 5)
    to_lazy_spec(lambda x: Left(x).to_lazy(), 'a', 'a')
test_Either_to_lazy.__test__ = False



# Generated at 2022-06-14 03:24:06.016853
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:24:10.205852
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_value = Right(3).to_lazy()
    assert lazy_value.value() == 3, 'Error in Either.to_lazy'
    assert lazy_value.map(lambda x: x * 2).value() == 6, 'Error in Either.to_lazy'



# Generated at 2022-06-14 03:24:13.713179
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Right(1).to_lazy()
    assert Lazy(lambda: 1) == Left(1).to_lazy()

# Generated at 2022-06-14 03:24:22.926977
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.box import Box

    try:
        assert Left('test').to_lazy().value() == 'test'
        assert Left(1 / 0).to_lazy().value() == 'test'
        assert Right('test').to_lazy().value() == 'test'
        assert Right(1 / 0).to_lazy().value() == 'test'
    except ZeroDivisionError:
        pass



# Generated at 2022-06-14 03:24:27.708499
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    '''
    :return:
    '''
    # Case either.is_left()
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    # Case either.is_right()
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    
    

# Generated at 2022-06-14 03:24:33.379426
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    def test_Either_to_lazy():
        from pymonet import Lazy
        from pymonet.either import Right

        assert Right([1, 2, 3]).to_lazy().get() == Lazy(lambda: [1, 2, 3]).get()
        assert Right("abc").to_lazy().get() == Lazy(lambda: "abc").get()
        assert Right(12).to_lazy().get() == Lazy(lambda: 12).get()
    """


# Generated at 2022-06-14 03:24:36.096403
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert isinstance(Right(42).to_lazy(), Lazy)

    assert Left(42).to_lazy() == Lazy(lambda: 42)
    assert isinstance(Left(42).to_lazy(), Lazy)


# Generated at 2022-06-14 03:24:40.323620
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:25:21.903402
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Test for class Left
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Left('A').to_lazy() == Lazy(lambda: 'A')

    # Test for class Right
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Right('A').to_lazy() == Lazy(lambda: 'A')


# Generated at 2022-06-14 03:25:23.726330
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy().value() == 5
    assert Left(5).to_lazy().value() == 5


# Generated at 2022-06-14 03:25:25.774014
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Left(1)) == Lazy(lambda: 1)
    assert Either.to_lazy(Right('test')) == Lazy(lambda: 'test')

# Generated at 2022-06-14 03:25:32.045193
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:25:37.569409
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Left("error").to_lazy() == Lazy(lambda: "error")


# Generated at 2022-06-14 03:25:52.898680
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def add(value, second_value):
        return value + second_value

    left = Left(2)
    right = Right(3)
    assert left.to_lazy().bind(add, right).value() == right.value
    assert right.to_lazy().bind(add, right).value() == add(right.value, right.value)



# Generated at 2022-06-14 03:25:56.351441
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:26:15.340052
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from functools import reduce

    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    def divide(a, b):
        return a / b

    def sub(a, b):
        return a - b

    def add_lazy(lazy_a, lazy_b):
        return Lazy(lambda: add(lazy_a.value(), lazy_b.value()))

    def mul_lazy(lazy_a, lazy_b):
        return Lazy(lambda: mul(lazy_a.value(), lazy_b.value()))


# Generated at 2022-06-14 03:26:17.786412
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    assert Either(2).map(lambda x: x + 1).to_lazy().run()() == 3

# Generated at 2022-06-14 03:26:20.756339
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right('success').to_lazy() == Lazy(lambda: 'success')
