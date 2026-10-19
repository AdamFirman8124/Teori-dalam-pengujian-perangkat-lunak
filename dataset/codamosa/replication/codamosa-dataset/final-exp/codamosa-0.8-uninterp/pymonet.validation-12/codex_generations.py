

# Generated at 2022-06-14 04:11:33.346210
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Perform unit tests for to_lazy method of class Validation.
    """
    def _test():
        """
        Function for testing.
        """

    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(_test)

    assert Validation.fail(['error']).to_lazy() == Lazy(_test)


# Generated at 2022-06-14 04:11:38.986836
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(4).to_lazy()
    assert isinstance(validation, Lazy)
    assert validation() == 4

    validation = Validation.fail([2, 3]).to_lazy()
    assert isinstance(validation, Lazy)
    assert validation() is None


# Generated at 2022-06-14 04:11:43.278475
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test for map method for List monad
    """
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    success = Validation.success(7)
    lazy = success.to_lazy()
    assert lazy.value() == Lazy(lambda: 7).value()



# Generated at 2022-06-14 04:11:47.075211
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    f = Lazy(lambda: 1 + 2)
    v = Validation.success(f)
    assert v.to_lazy() == f

# Generated at 2022-06-14 04:11:51.261998
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validate = Validation.success(2)
    lazy = validate.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 2
    assert lazy.is_forced is True


# Generated at 2022-06-14 04:11:54.478878
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(value=10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 04:11:59.263747
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pylint: disable=no-self-use,invalid-name
    """
    Test for Validation to_lazy method.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'value') == Validation.success('value').to_lazy()


# Generated at 2022-06-14 04:12:04.666454
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy of Validation class.
    """
    from pymonet.lazy import Lazy

    def run_lazy(lazy):
        return lazy.value()

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([10]).to_lazy().value() is None
    assert Lazy(lambda: 10).to_validation().is_success()
    assert not Lazy(lambda: Exception('error')).to_validation().is_success()

# Generated at 2022-06-14 04:12:07.123279
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def f():
        return Validation.success(3)
    lazy = f().to_lazy()
    assert lazy.value() == 3


# Generated at 2022-06-14 04:12:10.079402
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation(Try(1), ['fail'])

    lazy = validation.to_lazy()

    assert lazy == Lazy(lambda: validation.value)


# Generated at 2022-06-14 04:12:25.597395
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.either import Right, Left
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    validation = Validation.success(1)

    assert validation.to_lazy().to_monad() == Lazy(lambda: 1)
    assert validation.to_maybe().to_monad() == Maybe.just(1)
    assert validation.to_box().to_monad() == Box(1)
    assert validation.to_try().to_monad() == Try(1, is_success=True)
    assert validation.to_either().to_monad() == Right(1)

    validation = Validation.success(None)

   

# Generated at 2022-06-14 04:12:38.660403
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Map each 'to_lazy' method test to LazyUnitTest. Assert that result of
    each case has expected value.
    """
    from pymonet.lazy import Lazy
    from pymonet.test.lazy_unit_test import LazyUnitTest

    lazy_unit_tests = [
        LazyUnitTest(Validation.fail(errors=[1]), lambda: None, 'Validation.fail[None, [1]]'),
        LazyUnitTest(Validation.success(2), lambda: 2, 'Validation.success[2]')
    ]
    for lazy_unit_test in lazy_unit_tests:
        # Arrange
        lazy_unit_test.lazy = lazy_unit_test.monad.to_lazy()
        # Act & Assert

# Generated at 2022-06-14 04:12:43.761437
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy, delay

    assert Validation.success('abc').to_lazy() == Lazy(delay(lambda: 'abc'))
    assert Validation.fail('abc').to_lazy() == Lazy(delay(lambda: None))


# Generated at 2022-06-14 04:12:53.570483
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    val1 = Validation.success(123)
    val2 = Validation.fail(['asd', 'qwerty'])

    assert val1.to_lazy().get() == 123
    assert val2.to_lazy().get() is None

    assert val1.to_lazy().eval() == 123
    assert val2.to_lazy().eval() is None

    assert val1.to_lazy().map(lambda x: x + 222).eval() == 345
    assert val1.to_lazy().map(lambda x: x + 222).get() == 345

    assert val2.to_lazy().map(lambda x: x + 222).eval() is None
    assert val2.to_lazy().map(lambda x: x + 222).get() is None


# Generated at 2022-06-14 04:12:58.298520
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Lazy.of(1) == Lazy(lambda: 1)


# Generated at 2022-06-14 04:13:03.857439
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    value = 3

    assert Lazy(lambda: value) == Validation.success(value).to_lazy()
    assert Lazy(lambda: None) == Validation.fail(['error']).to_lazy()

# Generated at 2022-06-14 04:13:13.751199
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    def square(x):  # pragma: no cover
        return x * x

    def to_validation_with_try(x):  # pragma: no cover
        try:
            return Validation.success(square(x))
        except Exception as e:
            return Validation(None, [e])

    assert to_validation_with_try(2).to_lazy() == Lazy(lambda: 4)
    assert to_validation_with_try(2).to_lazy() == Lazy(lambda: 2 * 2)

# Generated at 2022-06-14 04:13:18.203530
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """

    result = Validation.fail(["some error"]).map(lambda a: a + 1).to_lazy()
    assert result.value() is None # pylint: disable=no-member

    result = Validation.success(1).map(lambda a: a + 1).to_lazy()
    assert result.value() == 2 # pylint: disable=no-member


# Generated at 2022-06-14 04:13:21.592523
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(3).to_lazy().run() == 3
    assert Validation.fail(['error']).to_lazy().run() is None


# Generated at 2022-06-14 04:13:26.775815
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(errors=[1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:37.580124
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test case for method to_lazy of class Validation
    """
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    success = Validation.success(10)
    fail = Validation.fail([10])

    assert success.to_lazy() == Lazy(lambda: 10)
    assert fail.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:13:40.889140
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Success, Failure

    def function():
        return 2

    assert Lazy(function) == Validation.success(2).to_lazy()


# Generated at 2022-06-14 04:13:45.710525
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return 3

    assert Validation.success(f).to_lazy() == Lazy(f)
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)



# Generated at 2022-06-14 04:13:48.218140
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(42).to_lazy()
    assert validation == Lazy(lambda: 42)



# Generated at 2022-06-14 04:13:51.293345
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(True).to_lazy() == Lazy(lambda: True)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:58.277363
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation('validation', [])

    lazy = validation.to_lazy()
    assert lazy.is_instance_of(Lazy)
    assert lazy.is_success()

    validation = Validation(None, ['error'])
    lazy = validation.to_lazy()
    assert lazy.is_instance_of(Lazy)
    assert lazy.is_success()
    assert lazy.value() is None

    assert validation.is_fail()
test_Validation_to_lazy()


# Generated at 2022-06-14 04:14:02.516335
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:06.797634
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    lazy = validation.to_lazy()

    assert lazy.value() == 1



# Generated at 2022-06-14 04:14:09.130620
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    unit_test(Lazy(lambda: 'success'), Validation('success', []).to_lazy())


# Generated at 2022-06-14 04:14:12.783706
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It tests Validation.to_lazy() method.
    """
    from pymonet.lazy import Lazy

    lazy = Validation.success(4).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.value() == 4

test_Validation_to_lazy()

# Generated at 2022-06-14 04:14:19.659261
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(2, []).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 04:14:28.381250
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def return_value(value):
        return value

    def return_none():
        return None

    validation = Validation(5, errors=[])
    lazy = validation.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.force() == 5
    validation = Validation(None, errors=[])
    lazy = validation.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.force() == None



# Generated at 2022-06-14 04:14:39.811383
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def add(a, b):
        return a + b

    def repeat_errors(errors):
        return errors + errors

    def twice(x):
        return x + x

    def increment(x):
        return x + 1

    assert Validation.success(add(1, 2)).to_lazy() == Lazy(3)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(None)
    assert increment(Validation.fail([]).to_lazy()) == Lazy(1)
    assert increment(Validation.success(0).to_lazy()) == Lazy(1)
    assert increment(increment(Validation.success(0).to_lazy())) == Lazy(2)


# Generated at 2022-06-14 04:14:44.810981
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation(42, []).to_lazy() == Lazy(lambda: 42)
    assert Validation(None, []).to_lazy() == Lazy(lambda: None)
    assert Validation(None, [1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:47.318182
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:14:55.399001
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    async def async_f():
        return 1

    def f():
        return 2

    lazy = Lazy(f)
    lazy2 = Lazy(async_f)

    assert Validation.success(1).to_lazy() == lazy
    assert Validation.success(1).to_lazy() == lazy
    assert Validation.success(async_f()).to_lazy() == lazy2
    assert Validation.success(async_f()).to_lazy() == lazy2

# Generated at 2022-06-14 04:15:01.144601
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # Validation successful
    value = 5
    lazy = Validation.success(value).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == value

    # Try fail
    lazy = Validation.fail([5, 3]).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() is None


# Generated at 2022-06-14 04:15:06.627387
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation('foo', []) == Validation.success(Validation.to_lazy('foo')().value)
    assert Validation(None, ['foo']) == Validation.fail(Validation.to_lazy(None).errors)
# test_Validation_to_lazy


# Generated at 2022-06-14 04:15:09.264169
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return 1

    assert Validation.success(1).to_lazy() == Lazy(f)


# Generated at 2022-06-14 04:15:12.036682
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(True).to_lazy() == Lazy(lambda: True)
    assert Validation.fail(True).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:24.007896
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:31.025780
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    v1 = Validation.success(1)
    v2 = Validation.fail(errors=[1, 2, 3])
    if Lazy(lambda: v1.value) != v1.to_lazy():  # pragma: no cover
        raise AssertionError('Validation.to_lazy() is wrong')
    if Lazy(lambda: v2.value) != v2.to_lazy():  # pragma: no cover
        raise AssertionError('Validation.to_lazy() is wrong')


# Generated at 2022-06-14 04:15:32.699505
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.success(1).to_lazy()

    assert 1 == lazy()


# Generated at 2022-06-14 04:15:35.927290
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    assert Lazy(lambda: 2) == Validation(2, []).to_lazy()


# Generated at 2022-06-14 04:15:42.296568
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)

    assert Validation.fail(['foo', 'bar']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['foo bar']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:45.782758
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:49.917389
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')
    assert Validation.fail(['wrong']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:52.994092
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    lazy = Lazy(lambda: 18)
    result = Validation.success(lazy)
    assert result.to_lazy() == lazy



# Generated at 2022-06-14 04:15:58.366016
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    test Validation.to_lazy method
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:01.474064
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    validation = Validation.success(1)
    assert isinstance(validation.to_lazy(), Lazy)


# Generated at 2022-06-14 04:16:18.429606
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    fn = lambda: 2
    assert Validation.success(2).to_lazy().force() == fn()

# Generated at 2022-06-14 04:16:23.750040
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.success(Lazy(lambda: 10))
    assert val.to_lazy() == Lazy(lambda: 10)
    assert val.to_lazy().value() == 10


# Generated at 2022-06-14 04:16:32.016632
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.validation import Validation as V

    success_lazy = V.success('sucess').to_lazy()
    assert isinstance(success_lazy, Lazy)
    assert success_lazy() == 'sucess'
    assert success_lazy.get() == 'sucess'

    fail_lazy = V.fail(['fail']).to_lazy()
    assert isinstance(fail_lazy, Lazy)
    assert fail_lazy() is None
    assert fail_lazy.get() is None


# Generated at 2022-06-14 04:16:33.764161
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def func():
        return 5

    validation = Validation.success(func)

    lazy = validation.to_lazy()

    assert func() == lazy.value()

# Generated at 2022-06-14 04:16:39.212265
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    Validation.success(1).to_lazy().map(lambda v: Try.success(v + 1)).value().map(lambda v: v + 1) == Lazy(lambda: Try.success(3))
    Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:42.343359
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # given
    validation = Validation.success(5)

    # when
    lazy_validation = validation.to_lazy()

    # then
    assert lazy_validation.value() == 5
    assert lazy_validation.is_lazy() == False

# Generated at 2022-06-14 04:16:47.127011
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(3)
    assert(validation.to_lazy() == Lazy(lambda: 3))

    validation = Validation.success()
    assert(validation.to_lazy() == Lazy(lambda: None))

    validation = Validation.fail()
    assert(validation.to_lazy() == Lazy(lambda: None))



# Generated at 2022-06-14 04:16:52.962320
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    success = Validation.success('hello')
    fail = Validation.fail(['error'])

    lazy = success.to_lazy()
    assert lazy.eval() == success.value

    lazy = fail.to_lazy()
    assert lazy.eval() == fail.value


# Generated at 2022-06-14 04:16:55.926830
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation('a', []).to_lazy() == Lazy(lambda: 'a')
    assert Validation(None, ['Error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:03.085068
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.list import List
    from pymonet.lazy import Lazy
    from pymonet.monad_try import monad_try_unit
    from pymonet.monad_try import Try
    from pymonet.monad_try_error import monad_try_error_unit

    # Given
    list_of_strings = List.of('abc')
    validation = Validation.success(list_of_strings)

    # When
    lazy_monad = validation.to_lazy()

    # Then
    assert lazy_monad.run() == list_of_strings


# Generated at 2022-06-14 04:17:21.389932
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given
    from pymonet.lazy import Lazy
    validation = Validation.success(5)

    # When
    lazy = validation.to_lazy()

    # Then
    assert lazy == Lazy(lambda: 5)



# Generated at 2022-06-14 04:17:27.181760
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    validation = Validation(5, [])
    lazy = validation.to_lazy()
    assert lazy.evaluate() == Lazy(lambda: validation.value)
    assert lazy.evaluate() == Lazy(lambda: 5)
    assert lazy.evaluate() == Lazy(lambda: 5).evaluate()

# Generated at 2022-06-14 04:17:29.270546
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.success(10)
    lazy = val.to_lazy()

    assert lazy == Lazy(lambda: 10)


# Generated at 2022-06-14 04:17:36.431715
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success("success").to_lazy().expect() == "success"
    assert Validation.fail("fail").to_lazy().expect() == None

    assert Validation.success("success").to_lazy().to_try().expect() == "success"
    assert Validation.fail("fail").to_lazy().to_try().is_fail()


# Generated at 2022-06-14 04:17:39.500071
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1) == Validation.success(1).to_lazy().get()
    assert Validation.fail(['error 1']) == Validation.fail(['error 1']).to_lazy().get()


# Generated at 2022-06-14 04:17:49.146504
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def get_user():
        return {'name': 'Piotr', 'age': 34}

    def validate_age(user):
        if user['age'] < 18:
            return Validation.fail(['User is too young'])
        return Validation.success(user)

    def validate_name(user):
        if user['name'].isalpha():
            return Validation.success(user)
        return Validation.fail(['Name contains wrong characters'])

    def validate_user(user):
        return validate_age(user).bind(validate_name).map(lambda _: user)

    user = validate_user(get_user()).to_lazy().value()

    assert user['age'] == 34

    def get_user():
        return {'name': 'Piotr', 'age': 9}

   

# Generated at 2022-06-14 04:17:56.292487
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation

    :return: None
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    value = Lazy(lambda: Validation(1, [2]))
    assert value.to_try() == Try(Validation(1, [2]), is_success=False)
    value = Lazy(lambda: Validation(1, []))
    assert value.to_try() == Try(Validation(1, []), is_success=True)


# Generated at 2022-06-14 04:17:58.858134
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)


# Generated at 2022-06-14 04:18:01.034314
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert(Validation.success(10).to_lazy() == Lazy(lambda: 10))


# Generated at 2022-06-14 04:18:09.610067
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    # Case: Validation has no errors and value equals 5
    v = Validation(5, [])
    lazy = v.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: 5)

    # Case: Validation has errors and value equals None
    v = Validation(None, [1, 2, 3])
    lazy = v.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: None)

# Generated at 2022-06-14 04:18:54.356545
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def ok():
        return Validation.success(1)

    def fail():
        return Validation.fail([1])

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)

    assert ok().to_lazy().force() == Validation.success(1)
    assert fail().to_lazy().force() == Validation.fail([1])

    add = Lazy(lambda : 1 + 1).force()
    assert ok().to_lazy().bind(lambda x: Lazy(lambda: x + add)).force() == Validation.success(3)
    assert fail().to_lazy().bind

# Generated at 2022-06-14 04:18:57.269241
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_monad = Validation.success(15).to_lazy()

    assert Validation.success(15) == lazy_monad.value()


# Generated at 2022-06-14 04:19:00.495299
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation.to_lazy should return Lazy monad.

    :returns: assertion error
    :rtype: AssertionError
    """

    assert Validation('Success', []).to_lazy() == Lazy(lambda: 'Success')


# Generated at 2022-06-14 04:19:03.508588
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    >>> v = Validation.success(1).map(lambda x: x ** 2).to_lazy()
    >>> v()
    1
    """


# Generated at 2022-06-14 04:19:05.712729
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def call():
        return 99
    lazy = Validation.success(call).to_lazy()
    assert lazy.evaluate() == 99


# Generated at 2022-06-14 04:19:12.047389
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import success, fail

    for errors, value in [
        ([], 1),
        (['error 1', 'error 2'], 1),
        ([], None),
        (['error 1', 'error 2'], None)
    ]:
        validation = Validation(value, errors)
        lazy_monad = Lazy(lambda: validation.value)
        assert validation.to_lazy() == lazy_monad
        assert lazy_monad._is_successful == validation.is_success()

# Generated at 2022-06-14 04:19:17.368173
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(42, []) == Lazy(lambda: Validation(42, [])).to_validation()
    assert Validation(None, []) == Lazy(lambda: Validation(None, [])).to_validation()


# Generated at 2022-06-14 04:19:21.456807
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validate_even = lambda x: Validation.success(x) if x % 2 == 0 else Validation.fail(['number is not even'])
    assert validate_even(2).to_lazy().force() == 2
    assert validate_even(3).to_lazy().force() is None


# Generated at 2022-06-14 04:19:27.802704
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    lazy = Validation.success(42).to_lazy()
    assert isinstance(lazy, Lazy), \
        'It should return lazy monad!'
    assert lazy.value() == 42, \
        'It should return 42!'
    try:
        Validation.fail(['Error']).to_lazy()
        assert False, \
            'It should throw exception!'
    except ValueError:
        pass


# Generated at 2022-06-14 04:19:34.102633
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.monad_try import TryException

    # Success value
    assert Lazy(lambda: 2).to_validation() == Validation(Lazy(lambda: 2))

    # Failed value
    assert (Lazy(lambda: Try(1 / 0)).to_validation() ==
            Validation(Lazy(lambda: Try(1 / 0)), [TryException()]))


# Generated at 2022-06-14 04:20:11.263261
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test():
        try:
            return Validation.success('hello')
        except:
            return Validation.fail('hello')
    validation = test()
    assert validation.to_lazy() == Lazy(lambda: 'hello')
    assert repr(validation.to_lazy()) == 'Lazy(lambda: function)'


# Generated at 2022-06-14 04:20:17.334234
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    val1 = Validation.success(1)
    val2 = Validation.fail(['error'])
    assert val1.to_lazy() == Lazy(lambda: 1), "Validation to Lazy test failed"
    assert val2.to_lazy() == Lazy(lambda: None), "Validation to Lazy test failed"


# Generated at 2022-06-14 04:20:21.746588
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)
    assert Validation.success().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:27.491520
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.success(42).to_lazy() != Lazy(lambda: None)
    assert Validation.fail(['Answer is wrong', 'Answer is not correct']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:31.027420
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda:1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda:None)


# Generated at 2022-06-14 04:20:34.127899
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    test = Validation.success(5)
    assert test.to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 04:20:42.663493
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(None).to_lazy() == Lazy(lambda: None)
    assert Validation.success(Try.success(1)).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(Try.success(1)).to_lazy() == Lazy(lambda: None)
    assert Validation.success(Try.fail(1)).to_lazy() == Lazy(lambda: None)
   

# Generated at 2022-06-14 04:20:49.456936
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test case for Validation to_lazy method.
    """

    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.success(5)
    assert validation.to_lazy() == Lazy(lambda: 5)

    validation = Validation.fail(['some-error'])
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:52.559422
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 0
    assert Validation.success().to_lazy() == Lazy(func)

# Generated at 2022-06-14 04:21:01.874324
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation to_lazy test

    :returns: None
    :rtype: None
    """
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)
