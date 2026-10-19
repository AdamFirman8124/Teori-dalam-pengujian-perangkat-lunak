

# Generated at 2022-06-14 04:11:38.391120
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    assert Validation.success(None) == Validation.success(None)
    assert Validation.success(10) == Validation.success(10)
    assert Validation.fail([]) == Validation.fail([])
    assert Validation.fail([1]) == Validation.fail([1])
    assert Validation.success() != Validation.fail()
    assert Validation.success() != Validation.fail([])
    assert Validation.success(10) != Validation.success()
    assert Validation.fail([]) != Validation.success()
    assert Validation.fail([1]) != Validation.fail([])
    assert Validation.fail([1]) != Validation.success(10)
    assert Validation.success(10) != Validation.fail([1])


# Generated at 2022-06-14 04:11:47.086742
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    assert Validation(1, ['error1', 'error2']) == Validation(1, ['error1', 'error2'])
    assert not Validation(1, ['error1', 'error2']) == Validation(2, ['error1', 'error2'])
    assert not Validation(1, ['error1']) == Validation(1, ['error1', 'error2'])
    assert not Validation(1, ['error1', 'error2']) == Validation(1, ['error1'])
    assert not Validation.success(1) == Validation(1, ['error1'])
    assert not Validation(1, ['error1']) == Validation.success(1)
    assert Validation.success(1) == Validation.success(1)

# Generated at 2022-06-14 04:11:50.099397
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    assert Validation.success('value').__eq__(None) is False
    assert Validation.fail(['error']).__eq__(None) is False


# Generated at 2022-06-14 04:11:52.533131
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def test_function(one, two):
        return Lazy(lambda: one + two)

    result = test_function(1, 2).force()
    assert result == 3

    result = test_function(10, 2).force()
    assert result == 12


# Generated at 2022-06-14 04:11:57.278497
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    assert Validation.success('1') == Validation.success('1')
    assert Validation.success('2') != Validation.success('1')

    assert Validation.fail(['1']) == Validation.fail(['1'])
    assert Validation.fail(['2']) != Validation.fail(['1'])


# Generated at 2022-06-14 04:12:00.991702
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functools import identity

    boxed = Validation.success(42).to_lazy()
    assert isinstance(boxed, Lazy)
    assert boxed == Lazy(identity(42))
    assert boxed.value == 42

# Generated at 2022-06-14 04:12:06.997893
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    # Test 1: success Validation with value
    assert Validation(1, [2]) != Validation(2, [2])
    assert Validation(1, [1]) != Validation(1, [2])
    assert Validation(1, [1]) != Validation(2, [1])

    # Test 2: success Validation with value
    assert Validation.success(1) == Validation.success(1)
    assert Validation.success(1) != Validation.success(2)

    # Test 3: fail Validation with value
    assert Validation.fail([1]) != Validation.fail([2])
    assert Validation.fail([1]) == Validation.fail([1])


# Generated at 2022-06-14 04:12:09.042630
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    from pymonet.either import Left, Right

    assert Validation.success() == Validation.success()
    assert Validation.fail() != Validation.fail()
    assert Validation.success('a') != Validation.success('b')
    assert Validation.fail('a') != Validation.fail('b')
    assert Validation.success() != Right()
    assert Validation.success() != Left()


# Generated at 2022-06-14 04:12:17.137409
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    """
    Unit test for method __eq__ of class Validation.
    """
    def test_equal():
        """
        Tests for equality of Validations
        """
        assert Validation.success(1) == Validation.success(1)
        assert Validation.fail([1]) == Validation.fail([1])
        assert (Validation.fail([1]) != Validation.fail([2]) or
                Validation.fail([1]) != Validation.success('b'))
    test_equal()


# Generated at 2022-06-14 04:12:23.897495
# Unit test for method __eq__ of class Validation
def test_Validation___eq__():
    # When
    validation1 = Validation(1, ['list of errors'])
    validation2 = Validation.success(1)
    validation3 = Validation.fail(['list of errors'])

    # Then
    assert validation1 == validation1
    assert validation1 == Validation(1, ['list of errors'])
    assert validation2 == validation2
    assert validation2 == Validation.success(1)
    assert validation3 == validation3
    assert validation3 == Validation.fail(['list of errors'])



# Generated at 2022-06-14 04:12:30.495437
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    result = Validation.success().to_lazy()
    assert isinstance(result, Lazy)

    result = Validation.success('value').to_lazy()
    assert callable(result.value)
    assert result.value() is None


# Generated at 2022-06-14 04:12:36.147002
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.validation import fail, success

    assert success(2).to_lazy() == Lazy(lambda: 2)
    assert fail().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:12:39.660708
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert(Validation.success(1).to_lazy() == Lazy(lambda: 1))


# Generated at 2022-06-14 04:12:42.566989
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    lazy_value = Lazy.unit(42)
    validation = Validation.success(lazy_value)
    try_result = validation.to_lazy()
    assert isinstance(try_result, Lazy)
    assert try_result.value() == Try.success(lazy_value)
    assert try_result.eval() == Try.success(42)


# Generated at 2022-06-14 04:12:52.373861
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(1, []).to_lazy() == Validation(1, []).to_lazy()
    assert not Validation(1, []).to_lazy() == Validation(2, []).to_lazy()
    assert Validation(None, [1]).to_lazy() == Validation(None, [1]).to_lazy()
    assert not Validation(None, [1]).to_lazy() == Validation(None, [2]).to_lazy()
    assert not Validation(1, []).to_lazy() == Validation(None, [1]).to_lazy()
    assert not Validation(None, [1]).to_lazy() == Validation(1, []).to_lazy()

# Generated at 2022-06-14 04:12:57.532816
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_function():
        return 'value'

    v = Validation.success()
    assert v.to_lazy().value() is None

    v = Validation.success(test_function)
    assert v.to_lazy().value() == test_function


# Generated at 2022-06-14 04:13:01.514548
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(3)
    assert validation.to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 04:13:03.867323
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def f():
        return 1
    assert Validation.success(f).to_lazy() == Lazy(f)


# Generated at 2022-06-14 04:13:07.007166
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation(1, []).to_lazy()
    assert lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 04:13:09.837746
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_function():
        return Validation(True, [])

    assert Validation.success(True).to_lazy() == Lazy(test_function)



# Generated at 2022-06-14 04:13:15.548440
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 14)
    assert lazy.to_validation() == Validation.success(14)

    lazy = Lazy(lambda: 'hello')
    assert lazy.to_validation() == Validation.success('hello')



# Generated at 2022-06-14 04:13:23.646990
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Failure
    from pymonet.monad_try import Success

    assert (
        Validation.success(10).to_lazy() == Lazy(lambda: 10) and
        Validation.fail([Failure.unit(Exception('Test'))]).to_lazy() == Lazy(lambda: None)
    )


# Generated at 2022-06-14 04:13:33.634144
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_maybe import Maybe
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    def check_successful_to_lazy(v):
        assert Lazy(lambda: v).to_monad().to_lazy() == Lazy(lambda: v)

    check_successful_to_lazy(Try.unit(1))
    check_successful_to_lazy(Maybe.unit(1))
    check_successful_to_lazy(Box.unit(1))
    check_successful_to_lazy(Lazy(lambda: 1))

if __name__ == '__main__':
    test_Validation_to_lazy()

# Generated at 2022-06-14 04:13:43.471373
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test that Validation to_lazy produces Lazy monad with function returning Validation value.
    """
    @unit_test('Validation.to_lazy')
    def test():
        """
        It is implementation of unit test for Validation.to_lazy function.
        """

        def test_validation():
            """
            Test Validation to_lazy on successful Validation.
            """
            validation = Validation.success(2)
            lazy = validation.to_lazy()
            return lazy.getop() == 2

        def test_validation_fail():
            """
            Test Validation to_lazy on failed Validation.
            """
            validation = Validation.fail(['1', '2', '3'])
            lazy = validation.to_lazy()
            return lazy.getop()

# Generated at 2022-06-14 04:13:45.810686
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(5, []).to_lazy().eval() == 5
    assert Validation(5, [1]).to_lazy().eval() == 5

# Generated at 2022-06-14 04:13:50.940099
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    result = Validation.success(5).to_lazy()
    assert isinstance(result, Lazy) and result.value() == 5

    result = Validation.fail([1, 2, 3]).to_lazy()
    assert isinstance(result, Lazy) and result.value() is None



# Generated at 2022-06-14 04:14:00.974186
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    class TestValidation:
        def __init__(self):
            self.result = None

        def test_method(self):
            self.result = 5

    class TestLazy:
        def __init__(self):
            self.result = None

        def call(self):
            self.test_method()

    t = TestValidation()
    t_lazy = TestLazy()
    t_lazy.call()

    assert t.result == t_lazy.result

    assert Validation.success(5).to_lazy().value() == 5
    assert Validation.fail([]).to_lazy().value() is None
    assert Validation.fail(['Failed validation']).to_lazy().value() is None



# Generated at 2022-06-14 04:14:01.996220
# Unit test for method to_lazy of class Validation

# Generated at 2022-06-14 04:14:11.413582
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation.to_lazy() returns Lazy with function returning value of the Validation.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    val = Validation.fail(["error"])
    lazy_monad = val.to_lazy()
    isinstance(lazy_monad, Lazy)
    isinstance(lazy_monad(), Try)

    val = Validation.success("value")
    lazy_monad = val.to_lazy()
    isinstance(lazy_monad, Lazy)
    isinstance(lazy_monad(), Try)



# Generated at 2022-06-14 04:14:21.345866
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    value = 10
    validation = Validation(value, [])

    lazy_monad = validation.to_lazy()
    assert isinstance(lazy_monad, Lazy)
    assert lazy_monad.value() == value

    validation = Validation(None, [1])
    lazy_monad = validation.to_lazy()
    assert isinstance(lazy_monad, Lazy)
    assert lazy_monad.value() is None


# Generated at 2022-06-14 04:14:29.402210
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    def fn():
        return 5

    success_validation = Validation.success(fn)
    fail_validation = Validation.fail()

    assert success_validation.to_lazy() == Lazy(fn)
    assert fail_validation.to_lazy() == Lazy(None)

# Unit tests for method to_try of class Validation

# Generated at 2022-06-14 04:14:37.560691
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().get() == 1
    assert Validation.success(None).to_lazy().get() is None
    assert Validation.fail([1]).to_lazy().get() is None
    assert Validation.fail(['f']).to_lazy().get() is None


# Generated at 2022-06-14 04:14:46.741723
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    Validation.fail(['error 1', 'error 2']) \
             .to_lazy() \
             .get() \
             .should_not_be_none()

    Validation.fail(['error 1', 'error 2']) \
             .to_lazy() \
             .get() \
             .should_be_equal(None)

    Validation.success('the value') \
             .to_lazy() \
             .get() \
             .should_not_be_equal(None)

    Validation.success('the value') \
             .to_lazy() \
             .get() \
             .should_be_equal('the value')


# Generated at 2022-06-14 04:14:52.803460
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation

    """
    from pymonet.lazy import Lazy
    validation = Validation(3, [])
    assert validation.to_lazy() == Lazy(lambda: 3)
    validation = Validation(None, [1, 2])
    assert validation.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:14:56.305789
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)

    assert Validation.fail([Error('err')]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:02.294216
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    successful_validation = Validation.success(2)
    assert successful_validation.to_lazy() == Lazy(lambda: successful_validation.value)

    failed_validation = Validation.fail(4)
    assert failed_validation.to_lazy() == Lazy(lambda: failed_validation.value)

# Generated at 2022-06-14 04:15:06.208245
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:09.925424
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(15).to_lazy() == Lazy(lambda: 15)
    assert Validation.fail([Error('Error!')]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:12.035028
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    l = Validation.success(1)
    assert l.to_lazy().get() == 1
    assert l.to_lazy().get() == 1


# Generated at 2022-06-14 04:15:16.208499
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:20.686173
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet import lazy
    val = Validation.success('abc')
    assert val.to_lazy() == lazy.Lazy(lambda: 'abc')


# Generated at 2022-06-14 04:15:23.867754
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.fail(["1"]).to_lazy() == Lazy(lambda: None)
    assert Validation.success('a').to_lazy() == Lazy(lambda: 'a')


# Generated at 2022-06-14 04:15:28.572061
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.either import Left
    from pymonet.box import Box

    v = Validation(Box(Left(['A'])), [])
    assert v.to_lazy().value().value().value() == ['A']

# Generated at 2022-06-14 04:15:32.309192
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:42.263377
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad import Monad

    class Some(Monad):

        def __init__(self, value):
            self.value = value

    success = Validation.success('a')
    lazy_with_value = success.to_lazy()

    assert isinstance(lazy_with_value, Lazy)
    assert lazy_with_value.get() == 'a'

    fail = Validation.fail(['error'])
    lazy_with_none = fail.to_lazy()

    assert isinstance(lazy_with_none, Lazy)
    assert lazy_with_none.get() is None



# Generated at 2022-06-14 04:15:48.857919
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert isinstance(Validation.success(42).to_lazy(), Lazy)
    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert isinstance(Validation.fail([0, 1]).to_lazy(), Lazy)
    assert Validation.fail([0, 1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:59.669790
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(None) == Validation.fail().to_lazy()

    assert Lazy(lambda: '1') == Validation.success(1).to_lazy().map(str)

    assert Lazy(None) == Validation.fail().to_lazy().map(lambda e: e + '2')

    assert Lazy(lambda: 1 + 2) == Validation.success(1).to_lazy().bind(
        lambda e: Lazy(lambda: e + 2))

# Generated at 2022-06-14 04:16:08.108004
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.either import Right

    assert(Validation.success('foo').to_lazy() == Lazy(lambda: 'foo'))
    assert(Validation.fail([]).to_lazy() == Lazy(lambda: None))
    assert(Validation.fail([]).to_lazy().map(lambda x: x.upper()) == Lazy(lambda: None))


# Generated at 2022-06-14 04:16:19.603717
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    actual = Validation.success(1).to_lazy()
    expected = Lazy(lambda: 1)
    assert actual == expected

    actual = Validation.fail([1, 2, 3]).to_lazy()
    assert actual == Lazy(lambda: None)

    actual = Validation.success(1).to_lazy().get_value()
    expected = Try(1, is_success=True)
    assert actual == expected

    actual = Validation.fail([1, 2, 3]).to_lazy().get_value()
    expected = Try(None, is_success=False)
    assert actual == expected

if __name__ == '__main__':
    import pytest

# Generated at 2022-06-14 04:16:24.173376
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    # Given
    validation = Validation.success(1)

    # When
    to_lazy = validation.to_lazy()

    # Then
    assert to_lazy().value == validation.value


# Generated at 2022-06-14 04:16:38.602827
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # GIVEN: Validation monad
    validation_success = Validation.success('Value')
    validation_fail = Validation.fail('Error')

    # WHEN: to_lazy is called
    lazy_success = validation_success.to_lazy()
    lazy_fail = validation_fail.to_lazy()

    # THEN: lazy monad should be returned
    assert isinstance(lazy_success, Lazy)
    assert isinstance(lazy_fail, Lazy)
    assert lazy_success.value == 'Value'
    assert lazy_fail.value == None



# Generated at 2022-06-14 04:16:44.915747
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Validation(5, []).to_lazy() == Lazy(lambda: 5)
    assert Validation(Box(5), []).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 04:16:48.620975
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert(Validation.success(1).to_lazy() == Lazy(lambda: 1))
    assert(Validation.fail([]).to_lazy() == Lazy(lambda: None))


# Generated at 2022-06-14 04:16:57.144461
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    val = Validation.success(2)
    lazy = val.to_lazy()

    assert (lazy == Lazy(lambda: 2))

    try:
        val.to_lazy()
    except Exception as e:
        raise AssertionError()

    err = 'error'
    val = Validation.fail([err])
    try:
        val.to_lazy()
        raise AssertionError()
    except Exception as e:
        assert (err in str(e))


# Generated at 2022-06-14 04:17:07.005360
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.monad_maybe import Maybe
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.monad_list import List
    from pymonet.either import Right, Left
    from pymonet.lazy import Lazy

    val = Validation.success(42)
    assert val.to_lazy() == Lazy(lambda: 42)
    val = Validation.success(42).to_maybe().to_lazy()
    assert val == Lazy(lambda: Maybe.just(42))
    val = Validation.success(42).to_box().to_lazy()
    assert val == Lazy(Box(42))

# Generated at 2022-06-14 04:17:12.447040
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.monad_list import List
    from pymonet.lazy import Lazy

    unit = Validation.fail()
    assert Lazy(lambda: None) == unit.to_lazy()

    value = 1
    unit = Validation.success(value)
    assert Lazy(lambda: value) == unit.to_lazy()


# Generated at 2022-06-14 04:17:15.263248
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy() method of class Validation.
    """
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 04:17:19.407804
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    assert Functor.fmap(Lazy(lambda: 3), lambda x: x ** 2) == Lazy(lambda: 9)


# Generated at 2022-06-14 04:17:25.734518
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy_success = Lazy(lambda: 1)
    assert Validation.success(1).to_lazy() == lazy_success

    lazy_fail = Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == lazy_fail


# Generated at 2022-06-14 04:17:28.741665
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success().to_lazy() == Lazy()
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([1, 2]).to_lazy() == Lazy()

# Generated at 2022-06-14 04:17:40.326154
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success("a").to_lazy()

    assert type(lazy) == Lazy
    assert lazy.get() == "a"
    assert str(lazy) == "Lazy[Function() -> a]"


# Generated at 2022-06-14 04:17:43.403185
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 1

    assert Validation.success(func()).to_lazy() == Lazy(func)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:17:48.565379
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    success_lazy = Lazy(lambda: 42)
    failed_lazy = Lazy(lambda: 0)

    assert Validation.fail().to_lazy() == failed_lazy
    assert Validation.success(42).to_lazy() == success_lazy



# Generated at 2022-06-14 04:17:53.688761
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    # Arrange
    value = 2
    validation = Validation.success(value)

    # Action
    lazy_validation = validation.to_lazy()

    # Assert
    assert lazy_validation is not None
    assert lazy_validation.get_value() == value



# Generated at 2022-06-14 04:17:59.746886
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # pylint: disable=R0204
    """
    It should create Lazy monad.
    """
    from pymonet.lazy import Lazy

    validation = Validation.success('Hello')
    lazy_monad = validation.to_lazy()

    assert Lazy == lazy_monad.__class__
    assert lazy_monad.fn() == 'Hello'

    validation = Validation.fail(['Some', 'Error'])
    lazy_monad = validation.to_lazy()

    assert Lazy == lazy_monad.__class__
    assert lazy_monad.fn() is None


# Generated at 2022-06-14 04:18:05.039210
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    success = Validation.success('ok')
    assert success.to_lazy() == Lazy(lambda: 'ok')

    fail = Validation.fail(['error'])
    assert fail.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:09.884857
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert(Validation.success('a').to_lazy() == Lazy(lambda: 'a'))

    assert(Validation.fail(['e1']).to_lazy() == Lazy(lambda: None))


# Generated at 2022-06-14 04:18:13.565056
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:17.250928
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    # Test when validation is successful
    assert Validation("a", []).to_lazy().map(lambda x: x.upper()) == Lazy("A")

    # Test when validation is failed
    assert Validation.fail([1, 2]).to_lazy().map(lambda x: x.upper()) == Lazy(None)



# Generated at 2022-06-14 04:18:24.266800
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy of class Validation.
    """
    import pymonet.lazy as lazy

    # when Validation is successful
    val = Validation.success(25)
    assert val.to_lazy() == lazy.Lazy(25)

    # when Validation is failed
    val = Validation.fail([])
    assert val.to_lazy() == lazy.Lazy(None)

# Generated at 2022-06-14 04:18:42.119138
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    get_nothing = Lazy(lambda: None)

    assert Validation.success().to_lazy() == Lazy(lambda: None)
    assert Validation.success(get_nothing).to_lazy() == Lazy(lambda: get_nothing)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.fail('error').to_lazy() == Lazy(lambda: None)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:18:45.705016
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 04:18:50.843861
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    # Given
    validation = Validation('Hello!', [])

    # When
    lazy = validation.to_lazy()

    # Then
    assert isinstance(lazy, Lazy)
    assert lazy() == 'Hello!'


# Generated at 2022-06-14 04:18:53.670352
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:18:58.876965
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.utils import inc

    assert Lazy(lambda: 10) == Validation.success(10).to_lazy()
    assert Lazy(lambda: inc(1)) == Validation.success(1).map(inc).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()


# Generated at 2022-06-14 04:19:08.324998
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail([2]).to_lazy() == Lazy(lambda: None)
    assert Validation.success([2]).to_lazy() == Lazy(lambda: [2])
    assert Validation.fail([2,3]).to_lazy() == Lazy(lambda: None)
    assert Validation.success([2, 3]).to_lazy() == Lazy(lambda: [2, 3])


# Generated at 2022-06-14 04:19:13.788351
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    assert Validation.fail('x is not number').to_lazy() == Lazy(lambda: None)
    assert Validation.success('Hello').to_lazy() == Lazy(lambda: 'Hello')


# Generated at 2022-06-14 04:19:18.268267
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail([3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:20.577054
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 04:19:25.691491
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    val = Validation(42, [])
    assert val.to_lazy() == Lazy(lambda: 42)

    val = Validation(23, ['error 1', 'error 2'])
    assert val.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:48.270276
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # Lazy should be equal to Validation value
    assert Lazy(lambda: '123') == Validation('123').to_lazy()

# Generated at 2022-06-14 04:19:52.417869
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().eval() == Try(1, True)



# Generated at 2022-06-14 04:19:58.480083
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:20:02.018710
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:06.152585
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(5)
    lazy = validation.to_lazy()
    assert lazy == Lazy(lambda: 5)
    assert lazy.eval() == 5
    assert lazy.eval() == 5


# Generated at 2022-06-14 04:20:09.881150
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test that Validation.to_lazy gives Lazy with function returning value from Validation.
    """
    from pymonet.lazy import Lazy

    assert Validation.success(8).to_lazy() == Lazy(lambda: 8)


# Generated at 2022-06-14 04:20:15.617986
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    def func():
        raise Exception('exception')

    def func2():
        return 1

    validation1 = Validation.fail().to_lazy()
    validation2 = Validation.success(1).to_lazy().bind(Lazy(func))
    validation3 = Validation.success(1).to_lazy().fmap(lambda _: 2)
    validation4 = Validation.success(1).to_lazy().bind(Lazy(func2))

    assert Try(None, is_success=False) == validation1.to_try()
    assert Try(None, is_success=False) ==  validation2.to_try()
    assert Try(2, is_success=True) ==  validation3.to_

# Generated at 2022-06-14 04:20:19.213492
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    errors = ['1', '2', '3']

    assert Validation(2, errors).to_lazy().value() == 2
    assert Validation(None, errors).to_lazy().value() is None


# Generated at 2022-06-14 04:20:23.040648
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # When Validation has no value
    validation = Validation.success()
    assert validation.to_lazy() == Lazy(lambda: None)

    # When Validation has value
    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:20:27.491578
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet import Lazy

    val1 = Validation.success('Success')
    val2 = Validation.fail('Fail')

    assert val1.to_lazy() == Lazy(lambda: 'Success')
    assert val2.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:21:14.572253
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert validation.to_lazy()() == 1


# Generated at 2022-06-14 04:21:18.431601
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(10)
    lazy = validation.to_lazy()
    assert lazy.value() == validation.value
    assert lazy.is_success() == True

# Generated at 2022-06-14 04:21:23.565344
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation to_lazy should return Lazy monad
    """
    val = Validation.success(42)
    assert val.to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 04:21:30.154621
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy in class Validation.
    """

    def success():
        return Validation.success()

    def fail():
        return Validation.fail()

    assert success().to_lazy().thunk() == Validation.success().value
    assert fail().to_lazy().thunk() == Validation.fail().value
