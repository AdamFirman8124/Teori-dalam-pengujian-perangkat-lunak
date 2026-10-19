

# Generated at 2022-06-14 03:16:50.693843
# Unit test for method case of class Either
def test_Either_case():
    """
    Test case function of class Either.
    """
    import unittest

    class TestEitherCase(unittest.TestCase):
        """
        Test case function of class Either.
        """

        def test_when_right_should_be_result_of_success(self):
            """
            Test when Either is Right should be result of success handler.
            """
            right = Right(5)
            result = right.case(lambda x: x * 2, lambda x: x * 3)
            self.assertEqual(result, 15)

        def test_when_left_should_be_result_of_error(self):
            """
            Test when Either is Left should be result of error handler.
            """
            left = Left('Error')

# Generated at 2022-06-14 03:16:55.676106
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left = Left(11)
    right = Right(11)
    assert not (left == right)
    assert left == Left(11)
    assert right == Right(11)


# Generated at 2022-06-14 03:16:58.217058
# Unit test for method case of class Either
def test_Either_case():
    assert Right(1).case(lambda x: x, lambda x: x * 2) == 2
    assert Left(1).case(lambda x: x * 2, lambda x: x) == 2

# Generated at 2022-06-14 03:17:00.846736
# Unit test for method case of class Either
def test_Either_case():
    assert Left(1).case(
        lambda x: x + 1,
        lambda x: x + 2
    ) == 2
    assert Right(1).case(
        lambda x: x + 1,
        lambda x: x + 2
    ) == 3



# Generated at 2022-06-14 03:17:05.807334
# Unit test for method case of class Either
def test_Either_case():
    assert Left(0).case(lambda x: x + 10, lambda x: x - 10) == 0
    assert Right(0).case(lambda x: x + 10, lambda x: x - 10) == -10



# Generated at 2022-06-14 03:17:12.596876
# Unit test for method case of class Either
def test_Either_case():
    def times_two(a):
        return a * 2

    def minus_five(a):
        return a - 5

    right = Right(2)
    left = Left(3)

    assert right.case(minus_five, times_two) == 4
    assert left.case(minus_five, times_two) == -1



# Generated at 2022-06-14 03:17:18.053156
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right(1) != Left(1)
    assert Right(1) != Right(2)
    assert Right(1) != None
    assert not None == Right(1)
    assert not Right(1) == None


# Generated at 2022-06-14 03:17:27.672612
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy

    assert Right(0).to_lazy() == Lazy(lambda: 0)
    assert Left(0).to_lazy() == Lazy(lambda: 0)

    assert Right(Box(0)).to_lazy() == Lazy(lambda: Box(0))
    assert Left(Box(0)).to_lazy() == Lazy(lambda: Box(0))

    assert Right(Maybe(0)).to_lazy() == Lazy(lambda: Maybe(0))
    assert Left(Maybe(0)).to_lazy() == Lazy(lambda: Maybe(0))

    assert Right(Maybe.just(0)).to_lazy() == Lazy(lambda: Maybe.just(0))
    assert Left

# Generated at 2022-06-14 03:17:34.468270
# Unit test for method case of class Either
def test_Either_case():
    def _error_case(error_value):
        return error_value/2

    def _success_case(success_value):
        return success_value*2

    error_test = Left(4)
    assert_equal(error_test.case(_error_case, _success_case), 2)

    success_test = Right(3)
    assert_equal(success_test.case(_error_case, _success_case), 6)



# Generated at 2022-06-14 03:17:38.795167
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:17:46.852816
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left('a') != Left('b')
    assert Left('a') == Left('a')
    assert Right('a') != Right('b')
    assert Right('a') == Right('a')


# Generated at 2022-06-14 03:17:54.645040
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Either(1) == Either(1)
    assert Either(1) != Either(2)
    assert Left(1) == Left(1)
    assert Left(1) != Left(2)
    assert Right(1) == Right(1)
    assert Right(1) != Right(2)
    assert Left(1) != Right(1)


# Generated at 2022-06-14 03:17:59.288440
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    try:
        assert Right(1) == Right(1)
        assert Right(1) != Left([])
        assert Right(1) != Right(2)
        assert Left([]) == Left([])
        assert Left([]) != Left([1])
        assert Left([]) != Right(1)
    except AssertionError:
        return False

    return True


# Generated at 2022-06-14 03:18:03.595767
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Left(2)) == Either.to_lazy(Right(2))
    from pymonet.lazy import Lazy
    assert isinstance(Either.to_lazy(Left(2)), Lazy)



# Generated at 2022-06-14 03:18:07.212185
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Left(1) != Right(1)
    assert Left(1) != Right(2)


# Generated at 2022-06-14 03:18:13.882576
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left('').__eq__(Left(''))
    assert not Left('').__eq__(Left('1'))
    assert not Left('').__eq__(Right(''))
    assert Right('').__eq__(Right(''))
    assert not Right('').__eq__(Right('1'))
    assert not Right('').__eq__(Left(''))

# Generated at 2022-06-14 03:18:19.514188
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right(1) != Right(2)
    assert Right(1) != Left(1)
    assert Right(1) != Box(1)
    assert Right(1) != Try(1)
    assert Right(1) != Lazy(lambda: 1)

# Generated at 2022-06-14 03:18:24.494375
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right(1) != Left(1)
    assert Left(1) != Right(1)
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)


# Generated at 2022-06-14 03:18:28.582825
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)
    assert Left(1) != 1
    assert Right(1) != 1


# Generated at 2022-06-14 03:18:31.009381
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Left(1) != Left(2)
    assert Right(1) != Left(1)


# Generated at 2022-06-14 03:18:36.675488
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left("error").to_lazy().get() == "error"
    assert Right("success").to_lazy().get() == "success"



# Generated at 2022-06-14 03:18:40.338170
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try

    lazy_right = Right(5).to_lazy()
    assert lazy_right.value() == 5

    lazy_left = Left(5).to_lazy()
    assert lazy_left.value() == 5



# Generated at 2022-06-14 03:18:43.480270
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 1)
    assert Right(1).to_lazy() == lazy
    assert Left(1).to_lazy() == lazy

# Generated at 2022-06-14 03:18:52.737102
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.functor import Functor
    from pymonet.lazy import Lazy
    import unittest

    class TestEitherToLazy(unittest.TestCase):
        def test_Left(self):
            self.assertEqual(
                Left('error').to_lazy(),
                Lazy(lambda: 'error')
            )

        def test_Right(self):
            self.assertEqual(
                Right(1).to_lazy(),
                Lazy(lambda: 1)
            )

    unittest.main()


# Generated at 2022-06-14 03:18:55.464501
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy().force() == 1
    assert Right(Lazy(lambda: 2)).to_lazy().force().force() == 2

# Generated at 2022-06-14 03:19:04.066327
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 4) == Right(4).to_lazy()
    assert Lazy(lambda: 4) == Left(4).to_lazy()
    assert Lazy(lambda: Right(4)) == Right(Right(4)).to_lazy()
    assert Lazy(lambda: Left(4)) == Right(Left(4)).to_lazy()
    assert Lazy(lambda: Right(4)) == Left(Right(4)).to_lazy()
    assert Lazy(lambda: Left(4)) == Left(Left(4)).to_lazy()
    assert Lazy(lambda: "4") == Right("4").to_lazy()
    assert Lazy(lambda: "4") == Left("4").to_lazy()

# Generated at 2022-06-14 03:19:06.620831
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:10.420128
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    assert (Left(None).to_lazy() == Lazy(lambda: None))
    assert (Right(None).to_lazy() == Lazy(lambda: None))

# Generated at 2022-06-14 03:19:13.382570
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left('Error').to_lazy().eval() == 'Error'
    assert Right('Value').to_lazy().eval() == 'Value'



# Generated at 2022-06-14 03:19:15.449747
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:25.214240
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest
    from pymonet.lazy import Lazy
    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:38.099277
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Given
    either = Right(10)

    # When
    result = either.to_lazy()

    # Then
    assert isinstance(result, Lazy)
    assert result.value() == 10


# Generated at 2022-06-14 03:19:44.507101
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Run tests for to_lazy function of Either.
    """

    # True test
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)

    # False test
    assert Right(5).to_lazy() != 5



# Generated at 2022-06-14 03:19:53.057148
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Tests for method to_lazy of class Either"""
    from pymonet.lazy import Lazy
    from pymonet.lazy import Lazy
    from pymonet.test_helpers import assert_equals

    def test_transform_Right_to_lazy(self):
        """Test transform Right to Lazy"""
        assert_equals(Right(2).to_lazy(), Lazy(lambda: 2))

    def test_transform_Left_to_lazy(self):
        """Test transform Left to Lazy"""
        assert_equals(Left(2).to_lazy(), Lazy(lambda: 2))

#Unit test for method bind of class Either

# Generated at 2022-06-14 03:20:00.283189
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Either case() method should return first argument when called with Left and second
    one otherwise.
    """
    assert Left(2).to_lazy().value() == 2
    assert Right(2).to_lazy().value() == 2


# Unit tests for method ap of class Either

# Generated at 2022-06-14 03:20:02.420003
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN
    from pymonet.lazy import Lazy

    # WHEN
    lazy = Left(10).to_lazy()

    # THEN
    assert lazy == Lazy(lambda: 10)

# Generated at 2022-06-14 03:20:04.453690
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    :returns: nothing
    :rtype: none
    """
    assert Either(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:20:07.512172
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_2 = Either(2).to_lazy()
    assert isinstance(lazy_2, Lazy)
    assert lazy_2.value() == 2



# Generated at 2022-06-14 03:20:09.520381
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    a = Lazy(lambda: 8)()
    b = Right(8).to_lazy()

    assert a == b

# Generated at 2022-06-14 03:20:13.926009
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().get_value() == 1
    assert Left(1).to_lazy().get_value() == 1


# Generated at 2022-06-14 03:20:24.863887
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    assert Right(2).to_lazy().value() == 2


# Generated at 2022-06-14 03:20:27.437112
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:20:30.778609
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:20:34.176040
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test Either.to_lazy() method
    """
    lazy_left = Left(1).to_lazy()
    assert lazy_left.eval() == 1

    lazy_right = Right(2).to_lazy()
    assert lazy_right.eval() == 2


# Generated at 2022-06-14 03:20:37.289467
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either("Hello").to_lazy() == Lazy(lambda: "Hello")
    assert Either([]).to_lazy() == Lazy(lambda: [])


# Generated at 2022-06-14 03:20:38.429519
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(0).to_lazy() == Lazy(lambda: 0)


# Generated at 2022-06-14 03:20:39.979198
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:20:47.498342
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy_try_success: Lazy[Try[bool]]\
        = Either(True).to_try().to_lazy()
    assert lazy_try_success.eval().is_success()

    lazy_try_fail: Lazy[Try[bool]]\
        = Either(False).to_try().to_lazy()
    assert not lazy_try_fail.eval().is_success()


# Generated at 2022-06-14 03:20:50.550313
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(3).to_lazy().run() == 3
    assert Left(3).to_lazy().run() == 3

# Generated at 2022-06-14 03:20:52.507781
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Either(1).to_lazy(), Lazy)



# Generated at 2022-06-14 03:21:09.959008
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Either

    assert Either(42).to_lazy() == Lazy(lambda: 42)
    assert Either(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:21:12.724390
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Unit: Lazy[Function() -> 1]
    assert(Right(1).to_lazy() == Lazy(lambda: 1))
    assert(Left(1).to_lazy() == Lazy(lambda: 1))

# Generated at 2022-06-14 03:21:17.036266
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().result() == 1
    assert Either('abc').to_lazy().result() == 'abc'
    assert Either(1.0).to_lazy().result() == 1.0
    assert Either(True).to_lazy().result() == True
    assert Either(False).to_lazy().result() == False



# Generated at 2022-06-14 03:21:18.836082
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(7).to_lazy() == Lazy(lambda: 7)

# Generated at 2022-06-14 03:21:20.470070
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left('abc').to_lazy().value() == 'abc'
    assert Right('abc').to_lazy().value() == 'abc'



# Generated at 2022-06-14 03:21:23.318326
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Assign
    lazy = Left('error').to_lazy()

    # Act
    result = lazy.evaluate()

    # Assert
    assert result == 'error'


# Generated at 2022-06-14 03:21:28.350216
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def run(a, b):
        return a + b

    computed = Right(1).to_lazy().map(lambda x: run(x, 2))

    assert computed.value == 3


# Generated at 2022-06-14 03:21:32.073948
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(None).to_lazy() == Lazy(None)
    assert Left(2).to_lazy() == Lazy(2)
    assert Right(3).to_lazy() == Lazy(3)


# Generated at 2022-06-14 03:21:34.143639
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(1)
    assert Left("Error").to_lazy() == Lazy("Error")

# Generated at 2022-06-14 03:21:37.109596
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:22:09.096009
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:22:11.520124
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Left(1)).value() == Lazy(lambda: 1).value()
    assert Either.to_lazy(Right(1)).value() == Lazy(lambda: 1).value()


# Generated at 2022-06-14 03:22:23.724104
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(5).to_lazy().__eq__(Lazy(lambda: 5)), 'Failed test_Either_to_lazy'
    assert Right(5).to_lazy().__eq__(Lazy(lambda: 5)), 'Failed test_Either_to_lazy'


# Generated at 2022-06-14 03:22:29.908756
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    def value():
        return Box(3)

    assert isinstance(Left(3).to_lazy(), Lazy)
    assert isinstance(Right(3).to_lazy(), Lazy)
    assert isinstance(Left(value()).to_lazy().value(), Box)
    assert isinstance(Right(value()).to_lazy().value(), Box)
    assert Left(5).to_lazy().value() == 5
    assert Right(5).to_lazy().value() == 5


# Generated at 2022-06-14 03:22:31.954637
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:22:34.690089
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.list import List
    from pymonet.validation import Validation

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:22:45.349553
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Left('').to_lazy(), Lazy)
    assert isinstance(Left(None).to_lazy(), Lazy)
    assert isinstance(Left('').to_lazy(), Lazy)
    assert Left(1).to_lazy().get() == 1
    assert Left('').to_lazy().get() == ''
    assert Left(None).to_lazy().get() is None
    assert Left('').to_lazy().get() == ''

    assert isinstance(Right(1).to_lazy(), Lazy)
    assert isinstance(Right('').to_lazy(), Lazy)
    assert isinstance(Right(None).to_lazy(), Lazy)

# Generated at 2022-06-14 03:22:48.496519
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    x = Right(1).to_lazy()
    assert x.value() == 1
    y = Left(1).to_lazy()
    assert y.value() == 1

# Generated at 2022-06-14 03:22:51.122022
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    def f():
        return 6
    assert Either.to_lazy(Right(f)) == Lazy(f)



# Generated at 2022-06-14 03:22:55.453122
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    a = Right("value1")
    b = a.to_lazy()
    assert b() == "value1"
    assert a == b
    assert b.value is a.value

    a = Left("value2")
    b = a.to_lazy()
    assert b() == "value2"
    assert a == b
    assert b.value is a.value



# Generated at 2022-06-14 03:23:41.893942
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:23:44.221612
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    @pytest.fixture
    def lazy_right():
        return Right(1).to_lazy()

    assert lazy_right().value == 1



# Generated at 2022-06-14 03:23:48.042830
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:23:49.441839
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:24:01.284081
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Success

    assert Success(10).to_either().to_lazy() == Lazy(lambda: 10)
    assert Success(10.2).to_either().to_lazy() == Lazy(lambda: 10.2)
    assert Success(10.2j).to_either().to_lazy() == Lazy(lambda: 10.2j)
    assert Success('ahoj').to_either().to_lazy() == Lazy(lambda: 'ahoj')


# Generated at 2022-06-14 03:24:05.906488
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy_eval import force

    either = Right(1)
    assert isinstance(either.to_lazy(), Lazy)
    assert force(either.to_lazy()) == 1

    either = Left([])
    assert isinstance(either.to_lazy(), Lazy)
    assert force(either.to_lazy()) == []



# Generated at 2022-06-14 03:24:11.262397
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    try_ = Try(1, is_success=True)
    lazy = try_.to_lazy()
    assert lazy.get() == 1
    assert lazy.get() == 1
    assert isinstance(lazy, Lazy)
    assert isinstance(lazy.get(), int)

# Generated at 2022-06-14 03:24:19.324297
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right
    from pymonet.either import Left
    from nose.tools import assert_equal
    from nose.tools import assert_true
    from nose.tools import assert_false

    assert_equal(Right(3).to_lazy(), Lazy(lambda: 3))
    assert_equal(Left(3).to_lazy(), Lazy(lambda: 3))
    assert_true(Right(3).to_lazy().value() == 3)
    assert_true(Left(3).to_lazy().value() == 3)


# Generated at 2022-06-14 03:24:27.660549
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def test(value):
        def success():
            return value

        def error():
            return None

        return Either.to_lazy(value) == Lazy(success, error)

    assert test(Right(1)) and\
           test(Left(2)) and\
           test(Right(None)) and\
           test(Left(None)) and\
           test(Either(None)) and\
           test(Either(1)), \
        'test_Either_to_lazy: bad functions values'



# Generated at 2022-06-14 03:24:33.343731
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from functools import partial

    def _test_left(e: Left, expected: Lazy):
        assert e.to_lazy() == expected

    def _test_right(e: Right, expected: Lazy):
        assert e.to_lazy() == expected

    _test_left(Left(1), Lazy(partial(Left, 1)))
    _test_right(Right(1), Lazy(partial(Right, 1)))



# Generated at 2022-06-14 03:25:24.370466
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(2).to_lazy().force() == 2

# Test case Either.to_box

# Generated at 2022-06-14 03:25:26.200188
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right = Right("foo")
    assert right.to_lazy().value() == "foo"
    left = Left("bar")
    assert left.to_lazy().value() == "bar"


# Generated at 2022-06-14 03:25:30.286915
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(10).to_lazy().evaluate() == 10
    assert Either(None).to_lazy().evaluate() is None


# Generated at 2022-06-14 03:25:36.830214
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.
    
    :returns: AssertionError if test failed
    """
    assert Left(2).to_lazy().value() == Right(2).to_lazy().value() == 2


# Generated at 2022-06-14 03:25:39.032951
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:25:47.190872
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Run a test on method to_lazy of class Either.

    :returns: nothing
    :rtype: None
    """
    from pymonet.test.test_helpers import should_be, should_be_of_type

    should_be(Left(5).to_lazy().value(), 5)
    should_be(Right(5).to_lazy().value(), 5)
    should_be_of_type(Left(5).to_lazy(), Either[int])
    should_be_of_type(Right(5).to_lazy(), Either[int])



# Generated at 2022-06-14 03:25:51.328584
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of Either"""
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    # given
    either = Right(100)

    # when
    result = either.to_lazy()

    # then
    assert isinstance(result, Lazy)
    assert result.value() == 100


# Generated at 2022-06-14 03:25:55.617219
# Unit test for method to_lazy of class Either

# Generated at 2022-06-14 03:26:05.040600
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:26:11.238214
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 100)
    left_either = Left(100)
    right_either = Right(100)

    assert left_either.to_lazy() == lazy
    assert right_either.to_lazy() == lazy