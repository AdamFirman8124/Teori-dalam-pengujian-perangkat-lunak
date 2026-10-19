

# Generated at 2022-06-14 03:16:56.544100
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left1 = Left(1)
    left2 = Left(2)
    right1 = Right(1)
    right2 = Right(2)
    identical_left = Left(1)
    identical_right = Right(1)

    assert left1 is not None
    assert left1 == identical_left
    assert left1 != right1
    assert left1 != left2
    assert right1 == identical_right
    assert right1 != right2


# Unit tests for method case of class Either

# Generated at 2022-06-14 03:17:00.492463
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """
    The test for method __eq__ of class Either.
    """

    assert Left(1) == Left(1)
    assert Right(1) == Right(1)

    assert Left(1) != Left(2)
    assert Left(1) != Right(1)

    assert Right(1) != Right(2)
    assert Right(1) != Left(1)



# Generated at 2022-06-14 03:17:16.053893
# Unit test for method case of class Either
def test_Either_case():
    """Tests for case method of Either class"""

    some_number = 1
    some_string = 'some_string'
    some_other_string = 'some_other_string'
    some_list = [1, 2, 3]
    some_other_list = [4, 5, 6]
    some_addition = either.case(
        lambda num: 0,
        lambda num: num + 2
    )
    some_string_uppercase = either.case(
        lambda num: 0,
        lambda num: some_string.upper()
    )
    some_list_added = either.case(
        lambda num: 0,
        lambda num: some_list + some_other_list
    )

    assert some_addition == 3
    assert some_string_uppercase == 'SOME_STRING'

# Generated at 2022-06-14 03:17:20.686571
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    result = Left("error").to_lazy()
    assert isinstance(result, Lazy)
    assert result == Lazy(lambda: "error")



# Generated at 2022-06-14 03:17:22.996796
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)


# Unit tests for method map of class Either

# Generated at 2022-06-14 03:17:30.922290
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert (Left(0) == Left(0)) is True
    assert (Left(0) == Left(1)) is False
    assert (Left(0) == Right(0)) is False

    assert (Right(0) == Right(0)) is True
    assert (Right(0) == Right(1)) is False
    assert (Right(0) == Left(0)) is False


# Generated at 2022-06-14 03:17:34.112536
# Unit test for method case of class Either
def test_Either_case():
    assert Left(2).case(lambda x: x % 2, lambda _: 1) == 1
    assert Right(4).case(lambda _: 1, lambda x: x % 2) == 0

# Generated at 2022-06-14 03:17:46.119115
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    def test_left():
        left_1 = Left('error')
        left_2 = Left('error')
        left_3 = Left('different error')

        assert left_1 == left_2
        assert left_1 != left_3

    def test_right():
        right_1 = Right(1)
        right_2 = Right(1)
        right_3 = Right(2)

        assert right_1 == right_2
        assert right_1 != right_3

        assert right_1 != left_1
        assert left_1 != right_1

    left_1 = Left('error')
    left_2 = Left('error')
    left_3 = Left('different error')
    right_1 = Right(1)
    right_2 = Right(1)
    right_3 = Right(2)

    test_

# Generated at 2022-06-14 03:17:53.129149
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right('success').to_lazy() == Lazy(lambda: 'success')


# Generated at 2022-06-14 03:17:57.699915
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right("Test") == Right("Test")
    assert Left("Test") == Left("Test")
    assert Right("Test") != Left("Test")
    assert Left("Test") != Right("Test")


# Generated at 2022-06-14 03:18:05.100311
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    # when Either is Left
    expected = Lazy(lambda: Exception('Error'))
    actual = Left(Exception('Error')).to_lazy()
    assert actual == expected

    # when Either is Right
    expected = Lazy(lambda: 'Success')
    actual = Right('Success').to_lazy()
    assert actual == expected


# Generated at 2022-06-14 03:18:08.265041
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(2).to_lazy().call() == 2
    assert Either(2).to_lazy().call() == 2


# Generated at 2022-06-14 03:18:12.336301
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:18:16.197626
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_either: Either[int] = Right(4)
    assert right_either.to_lazy().eval() == 4

    left_either: Either[int] = Left(5)
    assert left_either.to_lazy().eval() == 5



# Generated at 2022-06-14 03:18:18.518829
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(3).to_lazy() == Lazy(lambda: 3)
    assert Right(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:18:21.842273
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Either.to_lazy(Right(5)), Lazy)
    assert isinstance(Either.to_lazy(Left('text')), Lazy)


# Generated at 2022-06-14 03:18:25.447771
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:18:27.227225
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    new_either = Right(10).to_lazy()
    assert new_either.value() == 10


# Generated at 2022-06-14 03:18:34.260115
# Unit test for method to_lazy of class Either

# Generated at 2022-06-14 03:18:36.221199
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 1) == Either.Left(1).to_lazy()
    assert Lazy(lambda: 1) == Either.Right(1).to_lazy()


# Generated at 2022-06-14 03:18:41.299118
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Left("fail").to_lazy() == Lazy(lambda: "fail")


# Generated at 2022-06-14 03:18:51.169985
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Left([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Some(4).to_lazy() == Lazy(lambda: 4)
    assert None.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:18:53.715299
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:18:59.880440
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    expected_value = 3
    expected_call_count = 1
    call_count = 0

    def return_some_value() -> int:
        nonlocal call_count
        call_count += 1

        return expected_value

    from pymonet.neither import Left, Right
    from pymonet.lazy import Lazy

    assert Right(return_some_value).to_lazy() == Lazy(return_some_value)
    assert Left(return_some_value).to_lazy() == Lazy(return_some_value)
    assert call_count == expected_call_count



# Generated at 2022-06-14 03:19:03.186653
# Unit test for method to_lazy of class Either

# Generated at 2022-06-14 03:19:11.701319
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Either
    from pymonet.either import Right
    from pymonet.either import Left
    from pymonet.box import Box

    assert Either.to_lazy(Right(5)) == Lazy(5)
    assert Either.to_lazy(Left(Box(5))) == Lazy(Box(5))
    assert Either.to_lazy(Right(Box(5))) == Lazy(Box(5))
    assert Either.to_lazy(Left(5)) == Lazy(5)



# Generated at 2022-06-14 03:19:12.965858
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right("").to_lazy() == Right("").value
    assert Left("").to_lazy() == Left("").value


# Generated at 2022-06-14 03:19:17.106937
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad import Container

    assert Container.unit(Left(None)).to_lazy() == Container.unit(None).to_lazy()
    assert Container.unit(Right(None)).to_lazy() == Container.unit(None).to_lazy()


# Generated at 2022-06-14 03:19:26.298145
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test that converts Either to Lazy and back.

    :return: none
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'a').to_either().to_lazy() == Lazy(lambda: 'a')
    assert Lazy(lambda: 'a').to_either().to_lazy().value == Lazy(lambda: 'a').value
    assert Right(Lazy(lambda: 'a')).to_lazy() == Lazy(lambda: 'a')
    assert Left(Lazy(lambda: 'a')).to_lazy() == Lazy(lambda: 'a')


# Generated at 2022-06-14 03:19:32.886895
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Assert that to_lazy on the instance of Either returns the correct value."""
    # Initialize
    value = 'value'
    either = Right(value)
    from pymonet.lazy import Lazy

    # Do the test
    actual_lazy = either.to_lazy()

    # Check results
    expected_lazy = Lazy(lambda: value)
    assert actual_lazy == expected_lazy


# Generated at 2022-06-14 03:19:41.468013
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 0) == Left(0).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()



# Generated at 2022-06-14 03:19:45.819570
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:49.358386
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:19:55.164344
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_result = Either.to_lazy(Right('test'))
    assert isinstance(lazy_result, Lazy)
    assert lazy_result() == 'test'


# Generated at 2022-06-14 03:20:00.298338
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def _test(either: Either[T], expected_result: Lazy):
        actual_result = either.to_lazy()
        assert actual_result == expected_result, 'Expected: {0}, actual: {1}'.format(expected_result, actual_result)

    _test(Right(1), Lazy(lambda: 1))
    _test(Left(1), Lazy(lambda: 1))

# Generated at 2022-06-14 03:20:06.753624
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Either("a string").to_lazy() == Lazy(lambda: "a string")
    assert Either(1.3).to_lazy() == Lazy(lambda: 1.3)
    assert Either("a string").to_lazy() == Lazy(lambda: "a string")
    assert Either(False).to_lazy() == Lazy(lambda: False)
    assert Either(True).to_lazy() == Lazy(lambda: True)
    assert Either(Right(True)).to_lazy() == Lazy(lambda: Right(True))

# Generated at 2022-06-14 03:20:07.896918
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(2).to_lazy(), Lazy)

# Generated at 2022-06-14 03:20:13.927797
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:20:16.402690
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    result = Either.to_lazy(Right(4))
    assert result == Lazy(lambda: 4)

# Generated at 2022-06-14 03:20:22.194064
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    assert Left("Error occurs").to_lazy() == Lazy(lambda: "Error occurs")
    assert Right("Done!").to_lazy() == Lazy(lambda: 'Done!')


# Generated at 2022-06-14 03:20:26.541443
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left("Bad").to_lazy() == Lazy(lambda: "Bad")


# Generated at 2022-06-14 03:20:31.695976
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    either = Right(1)

    # When
    lazy = either.to_lazy()

    # Then
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1

# Generated at 2022-06-14 03:20:39.520903
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy as lazy

    def identity(x): return x

    # if Either is Left do nothing
    assert lazy.map(identity, Left(3).to_lazy()) == lazy.map(identity, lazy.unit(3))

    # if Either is Right map its value
    assert lazy.map(identity, Right(3).to_lazy()) == lazy.map(identity, lazy.unit(3))


# Generated at 2022-06-14 03:20:46.127853
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    # Test for  method to_lazy of class Left
    assert Left('error').to_lazy() == Lazy(lambda: 'error')

    # Test for  method to_lazy of class Right
    assert Right(12).to_lazy() == Lazy(lambda: 12)

# Generated at 2022-06-14 03:20:54.163008
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN value
    value = 1

    # AND right Either based on value
    right_either = Right(value)

    # WHEN to_lazy is called
    result = right_either.to_lazy()

    # THEN it returns new instance of type Lazy
    assert isinstance(result, Lazy)

    # AND result is not None
    assert result.get() is not None

    # AND result is equal to value
    assert result.get() == value



# Generated at 2022-06-14 03:20:58.477648
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Either
    from pymonet.either import Left
    from pymonet.either import Right
    
    assert Lazy(lambda: 1) == Either(1).to_lazy()
    assert Lazy(lambda: 1) == Either(Right(1)).to_lazy()
    assert Lazy(lambda: 1) == Either(Left(1)).to_lazy()


# Generated at 2022-06-14 03:20:59.747464
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().get() == 1
    assert Left(2).to_lazy().get() == 2


# Generated at 2022-06-14 03:21:02.996234
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    monad = Either(10)
    result = monad.to_lazy()
    assert isinstance(result, Lazy)
    assert result.m_value() == 10



# Generated at 2022-06-14 03:21:05.566781
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(5).to_lazy().__str__() == 'Lazy result: 5'
    assert Right(5).to_lazy().__str__() == 'Lazy result: 5'


# Generated at 2022-06-14 03:21:08.022543
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    def func():
        return 1

    assert Right(1).to_lazy() == Lazy(func)

# Generated at 2022-06-14 03:21:15.843979
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from functools import reduce

    # When
    lazy_maybe = Either(2).to_lazy()

    # Then
    assert lazy_maybe == Lazy(lambda: 2)



# Generated at 2022-06-14 03:21:18.376556
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    result = Either(Box("foo")).to_lazy()
    assert result == Lazy(lambda: "foo")


# Generated at 2022-06-14 03:21:21.693380
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:21:24.147211
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(3).to_lazy().get() == 3
    assert Left('error').to_lazy().get() == 'error'


# Generated at 2022-06-14 03:21:31.049290
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Either.Left(5).to_lazy() == Lazy(lambda: 5)
    assert Either.Right(5).to_lazy() == Lazy(lambda: 5)
    assert Either.Left(5).to_lazy() != Lazy(lambda: 6)
    assert Either.Right(5).to_lazy() != Lazy(lambda: 6)


# Generated at 2022-06-14 03:21:34.638514
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Try(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:39.241718
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    # Given
    either = Left("error")
    # When
    result_lazy = either.to_lazy()
    # Then
    assert isinstance(result_lazy, Lazy)
    assert result_lazy.get() == "error"



# Generated at 2022-06-14 03:21:42.673602
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import unit as lazy_unit

    x = Right(10)
    assert x.to_lazy() == lazy_unit(10)

    x = Left(10)
    assert x.to_lazy() == lazy_unit(10)


# Generated at 2022-06-14 03:21:45.407826
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def f():
        return "Lazy evaluations"
    left = Left(0)
    actual = left.to_lazy()
    assert isinstance(actual, Lazy)
    assert actual.get_value() == 0


# Generated at 2022-06-14 03:21:50.473980
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    e1 = Right(10)
    assert e1.to_lazy().force() == 10
    e2 = Left(None)
    assert e2.to_lazy().force() is None


# Generated at 2022-06-14 03:22:02.948900
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Either(2).to_lazy()


# Generated at 2022-06-14 03:22:09.494940
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:22:14.420999
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Right('success').to_lazy() == Lazy(lambda: 'success')
    assert Left('failure').to_lazy() == Lazy(lambda: 'failure')



# Generated at 2022-06-14 03:22:16.497731
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    :returns: None
    :rtype: None
    """
    from pymonet.lazy import Lazy

    def inner_lazy():
        return "Some lazy value"

    assert Either(inner_lazy()).to_lazy() == Lazy(inner_lazy)



# Generated at 2022-06-14 03:22:23.797492
# Unit test for method to_lazy of class Either
def test_Either_to_lazy(): #pylint: disable=missing-function-docstring
    from pymonet.lazy import Lazy

    lazy_left = Left(1).to_lazy()
    assert isinstance(lazy_left, Lazy)
    assert lazy_left.value() == 1

    lazy_right = Right(1).to_lazy()
    assert isinstance(lazy_right, Lazy)
    assert lazy_right.value() == 1


# Generated at 2022-06-14 03:22:25.159315
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('value').to_lazy() == Lazy(lambda: 'value')
    assert Right('value').to_lazy() == Lazy(lambda: 'value')


# Generated at 2022-06-14 03:22:28.766248
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 0).equals(Right(0).to_lazy())
    assert Lazy(lambda: 1).equals(Right(1).to_lazy())
    assert Lazy(lambda: '2').equals(Right('2').to_lazy())


# Generated at 2022-06-14 03:22:40.370455
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy().value is Lazy(lambda: 1).value
    assert Left(1).to_lazy() is Lazy(lambda: 1)
    assert Right(1).to_lazy().value is Lazy(lambda: 1).value
    assert Right(1).to_lazy() is Lazy(lambda: 1)
    assert Either(Try(1)).to_lazy().value is Lazy(lambda: 1).value
    assert Either(Try(1)).to_lazy() is Lazy(lambda: 1)
    assert Either(Box(1)).to_lazy().value is Lazy(lambda: 1).value
    assert Either(Box(1)).to_

# Generated at 2022-06-14 03:22:43.751126
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    res = Either(1).to_lazy()
    assert isinstance(res, Lazy)
    assert res.get() == 1



# Generated at 2022-06-14 03:22:46.477528
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(3).to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:23:00.541029
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.Right(123).to_lazy() == Lazy(lambda: 123)



# Generated at 2022-06-14 03:23:02.928035
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(123).to_lazy().value() == 123


# Generated at 2022-06-14 03:23:04.672099
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right().to_lazy().evaluate() == None
    assert Left().to_lazy().evaluate() == None



# Generated at 2022-06-14 03:23:07.403293
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:23:10.727121
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    val = Right(10).to_lazy()
    assert isinstance(val, Lazy)
    assert val.value() == 10

    val = Left(10).to_lazy()
    assert isinstance(val, Lazy)
    assert val.value() == 10

# Generated at 2022-06-14 03:23:14.890820
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:23:20.438445
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:23:25.018376
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_unit = Either(5).to_lazy()
    assert isinstance(lazy_unit, Lazy)
    assert lazy_unit.get() == 5



# Generated at 2022-06-14 03:23:28.483455
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(Box(5)).to_lazy() == Lazy(lambda: Box(5))



# Generated at 2022-06-14 03:23:31.795157
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    either = Right(3).to_lazy()
    assert isinstance(either, Lazy)
    assert either.thunk() == 3
    assert Left(4).to_lazy().thunk() == 4



# Generated at 2022-06-14 03:23:58.777714
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(10).to_lazy().force() == 10
    assert Right(20).to_lazy().force() == 20



# Generated at 2022-06-14 03:24:02.965465
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert isinstance(Right(Box(1)).to_lazy(), Lazy)
    assert isinstance(Left(Box(1)).to_lazy(), Lazy)
    assert Right(Box(1)).to_lazy().value() == Box(1)
    assert Left(Box(1)).to_lazy().value() == Box(1)


# Generated at 2022-06-14 03:24:04.751117
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(None).to_lazy().force() is None
    assert Right(None).to_lazy().force() is None



# Generated at 2022-06-14 03:24:08.162302
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Test for Either with Left
    value = Left("error")
    assert value.to_lazy() == Lazy(lambda: "error")

    # Test for Either with Right
    value = Right("val")
    assert value.to_lazy() == Lazy(lambda: "val")



# Generated at 2022-06-14 03:24:15.220796
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Either(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()
    assert Lazy(lambda: 1) == Left(1).to_lazy()

    assert Lazy(lambda: 1) == Right(1).to_lazy()
    assert Lazy(lambda: 1) == Left(1).to_lazy()


# Generated at 2022-06-14 03:24:18.963709
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    @Lazy
    def lazy_inc(x):
        return x + 1
    assert lazy_inc(1) == Right(2).to_lazy()
    assert lazy_inc(5) == Left(5).to_lazy()

# Generated at 2022-06-14 03:24:22.376247
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Either.to_lazy(5)
    assert lazy == Lazy(lambda: 5)



# Generated at 2022-06-14 03:24:27.491627
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    value = 5

    # Test for Left
    old_left = Left(value)
    assert old_left.to_lazy() == Lazy(lambda: value)

    # Test for Right
    old_right = Right(value)
    assert old_right.to_lazy() == Lazy(lambda: value)



# Generated at 2022-06-14 03:24:30.308351
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Test to_lazy method of class Either"""
    from pymonet.lazy import Lazy

    result = Right(5).to_lazy()

    assert result == Lazy(lambda: 5)



# Generated at 2022-06-14 03:24:34.180049
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Right(12)) == Lazy(lambda: 12)
    assert Either.to_lazy(Left("error")) == Lazy(lambda: "error")
    print("test_Either_to_lazy finished successfully")


# Generated at 2022-06-14 03:25:00.031617
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    right = Right(5)
    assert right.to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:25:06.717839
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy
    import random

    value = random.randint(0, 100)

    lazy_left = Left(value).to_lazy()
    assert lazy_left.force() == value
    assert lazy_left.value() == Lazy(lambda: value)

    lazy_right = Right(value).to_lazy()
    assert lazy_right.force() == value
    assert lazy_right.value() == Lazy(lambda: value)

# Generated at 2022-06-14 03:25:11.589090
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box

    def add_5_to_value(box: Box[int]) -> Box[int]:
        return box.map(lambda x: x + 5)

    assert Right(Box(5)).to_lazy().bind(add_5_to_value).value.value == 10
    assert Left(Box(5)).to_lazy().bind(add_5_to_value).value.value == 5


# Generated at 2022-06-14 03:25:16.362177
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().computation() == 1
    assert Right(1).to_lazy().computation() == 1



# Generated at 2022-06-14 03:25:24.758819
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def assert_equal(item: Lazy[int], expected: Lazy[int]):
        assert item == expected

    def assert_not_equal(item: Lazy[int], expected: Lazy[int]):
        assert item != expected

    lazy_value = Lazy(lambda: 1)
    right = Right(1)
    left = Left(1)

    assert_equal(
        right.to_lazy(),
        lazy_value
    )

    assert_equal(
        left.to_lazy(),
        lazy_value
    )

    assert_not_equal(
        right.to_lazy(),
        Lazy(lambda: 2)
    )


# Generated at 2022-06-14 03:25:26.575926
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(123).to_lazy().force() == 123
    assert Left(123).to_lazy().force() == 123
    assert Right(123).to_lazy().force() == 123



# Generated at 2022-06-14 03:25:39.840336
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.identity import Identity
    from pymonet.box import Box

    assert Either(Identity(42)).to_lazy() == Lazy(lambda: Identity(42))
    assert Either(Box(42)).to_lazy() == Lazy(lambda: Box(42))
    assert Either(Either(42)).to_lazy() == Lazy(lambda: Either(42))
    assert Left(42).to_lazy() == Lazy(lambda: 42)
    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Either(Lazy(lambda: 42)).to_lazy() == Lazy(lambda: Lazy(lambda: 42))


# Generated at 2022-06-14 03:25:42.519417
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5).eval() == Right(5).to_lazy().eval()



# Generated at 2022-06-14 03:25:44.296516
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:25:49.508285
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(2).to_lazy() == Lazy(lambda: 2) and Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:26:28.577099
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    result = Right(False).to_lazy()
    assert isinstance(result, Lazy) and isinstance(result.value(), bool)
    result = Left(35).to_lazy()
    assert isinstance(result, Lazy) and isinstance(result.value(), int)


# Generated at 2022-06-14 03:26:32.126776
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(10).to_lazy() == Lazy(lambda: 10)
    assert Right(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 03:26:44.749599
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)

