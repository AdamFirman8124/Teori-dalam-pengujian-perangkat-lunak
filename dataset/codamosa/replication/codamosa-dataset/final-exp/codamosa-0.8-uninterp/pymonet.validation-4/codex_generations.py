

# Generated at 2022-06-14 04:11:38.264305
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """Unit test for method to_lazy of class Validation."""

    # Given
    validation = Validation.success(1)
    validation_fail = Validation.fail([1, 2, 3])

    # When
    lazy = validation.to_lazy()
    lazy_fail = validation_fail.to_lazy()

    # Then
    assert lazy() == 1
    assert lazy_fail() is None
    assert validation == validation_fail == lazy == lazy_fail



# Generated at 2022-06-14 04:11:45.553717
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation_success = Validation.success()
    assert validation_success.to_lazy() == Lazy(lambda: None)

    validation_failure = Validation.fail()
    assert validation_failure.to_lazy() == Lazy(lambda: None)

    validation_success = Validation.success('value')
    assert validation_success.to_lazy() == Lazy(lambda: 'value')

    validation_failure = Validation.fail(['error'])
    assert validation_failure.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:11:51.300367
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import TryException
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 15) == Validation.success(15).to_lazy()
    assert Lazy(lambda: 0.45) == Validation.success(0.45).to_lazy()
    assert Lazy(lambda: 'hello') == Validation.success('hello').to_lazy()
    assert Lazy(lambda: [1, 2, 3]) == Validation.success([1, 2, 3]).to_lazy()
    assert Lazy(lambda: ()) == Validation.success(()).to_lazy()
    assert Lazy(lambda: {1, 2, 3}) == Validation.success({1, 2, 3}).to_lazy()

# Generated at 2022-06-14 04:11:53.977676
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 4) == Validation.success(4).to_lazy()

# Generated at 2022-06-14 04:11:58.212512
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(Lazy(lambda: 5))
    result_validation = validation.to_lazy()

    assert result_validation.value() == 5

# Generated at 2022-06-14 04:12:02.631783
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def f(x):
        print("f is evaluated")
        return x

    # Successful Validation
    assert Lazy(f, x = 1) == Validation.success(x = 1).to_lazy()
    # Failed Validation
    assert Lazy(f, x = None) == Validation.fail(x = 1).to_lazy()

# Generated at 2022-06-14 04:12:04.860703
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    actual = Validation.success().to_lazy()
    expected = Lazy(lambda: None)

    assert actual == expected

# Generated at 2022-06-14 04:12:07.919079
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    expected = Lazy(lambda: 1)
    actual = Validation.success(1).to_lazy()

    assert expected == actual


# Generated at 2022-06-14 04:12:11.262481
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_val = Validation(1, []).to_lazy()
    assert lazy_val == Lazy(lambda: 1)

    lazy_val = Validation(1, [2, 3]).to_lazy()
    assert lazy_val == Lazy(lambda: 1)


# Generated at 2022-06-14 04:12:21.626255
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_try import Try

    lazy_monad = Validation.success(1).to_lazy()
    assert isinstance(lazy_monad, Lazy)
    assert lazy_monad() == Try(1, True)

    lazy_monad = Validation.fail(['Some error']).to_lazy()
    assert isinstance(lazy_monad, Lazy)
    assert lazy_monad() == Try(None, False)



# Generated at 2022-06-14 04:12:31.221170
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def f(x):
        return x
    def g(x):
        return x
    def h(x):
        return x

    x = Validation.success(1)

# Generated at 2022-06-14 04:12:36.338810
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def expected(x):
        return Lazy(lambda: x)

    def given(x):
        return Validation.success(x).to_lazy()

    return (given(1) == expected(1))

# Generated at 2022-06-14 04:12:39.404420
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    value = 1
    res = Validation.success(value).to_lazy()

    assert res.get() == value


# Generated at 2022-06-14 04:12:47.260134
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Failure

    validation = Validation.success(1)
    result = validation.to_lazy()
    assert result.is_successful() is True
    assert result.get() == 1

    validation = Validation.fail([Failure('Error')])
    result = validation.to_lazy()
    assert result.is_successful() is True
    assert result.get() is None


# Generated at 2022-06-14 04:12:50.222922
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # GIVEN
    validation = Validation.success(2)

    # WHEN
    lazy = validation.to_lazy()

    # THEN
    assert lazy == Lazy(lambda: 2)

# Generated at 2022-06-14 04:12:54.277292
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_func():
        return Validation.fail(['error'])

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail(['error']).to_lazy() == Lazy(lazy_func)

# Generated at 2022-06-14 04:12:58.972682
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def fun():
        return 1

    lazy_fun = Lazy(fun)
    val = Validation.success(1)
    assert val.to_lazy() == lazy_fun



# Generated at 2022-06-14 04:13:03.857581
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success('value').to_lazy()

    assert isinstance(lazy, Lazy)
    assert callable(lazy.value)
    assert lazy.value() == 'value'


# Generated at 2022-06-14 04:13:07.431094
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def as_lazy(value):
        return Validation.success(value).to_lazy()

    assert isinstance(as_lazy('value'), LAZY_TYPE)


# Generated at 2022-06-14 04:13:13.186883
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import call_if_needed
    from pymonet.validation import Validation

    validation = Validation.success(Lazy(lambda: 'value'))
    assert validation.to_lazy().value == Lazy(lambda: 'value')

    assert call_if_needed(validation.to_lazy()) == Lazy(lambda: 'value')


# Generated at 2022-06-14 04:13:18.128828
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert (Validation.fail([1, 2, 3]).to_lazy()
            == Lazy(lambda: None))
    assert (Validation.success(1).to_lazy()
            == Lazy(lambda: 1))

# Generated at 2022-06-14 04:13:23.761792
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Validation.success(Box(2)).to_lazy() == Lazy(lambda: Box(2))
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:32.438334
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    validation_1 = Validation.success()
    lazy_1 = validation_1.to_lazy()
    assert lazy_1 == Lazy(lambda: None)

    validation_2 = Validation.success(value=1)
    lazy_2 = validation_2.to_lazy()
    assert lazy_2 == Lazy(lambda: 1)

    validation_3 = Validation.fail()
    lazy_3 = validation_3.to_lazy()
    assert lazy_3 == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:38.244350
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:43.440612
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    success_validation = Validation.success(10)
    assert isinstance(success_validation.to_lazy(), Lazy)
    assert success_validation.to_lazy().get() == 10

    fail_validation = Validation.fail([5])
    assert isinstance(fail_validation.to_lazy(), Lazy)
    assert fail_validation.to_lazy().get() == None



# Generated at 2022-06-14 04:13:53.215885
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    import pymonet.lazy
    from pymonet.lazy import Lazy

    def unsafe_function(value):
        if value != 42:
            raise Exception('42 value not detected')
        return value

    unsafe_function_lazy = Lazy(lambda: unsafe_function)

    assert Validation.success(42).is_success() is True
    assert Validation.success(42).is_fail() is False
    assert Validation.fail(['42 value not detected']).is_success() is False
    assert Validation.fail(['42 value not detected']).is_fail() is True

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail(['42 value not detected']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:00.972218
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    def mock_method_call():
        """
        Method that raises Exception.

        :returns: None
        :rtype: None
        """
        raise Exception('Exception in method')

    v = Validation.success(42)
    assert v.to_lazy().eval() == 42
    assert v.to_lazy().get() == 42

    v = Validation.fail(['Error'])
    assert v.to_lazy().eval() is None
    assert v.to_lazy().get() is None

    # Method call raises an exception
    v = Validation.fail(['Error'])
    assert v.to_lazy(mock_method_call).eval() is None

# Generated at 2022-06-14 04:14:06.170525
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_value():
        return 1

    assertion = Validation(lazy_value, [])
    result = assertion.to_lazy()

    assert result == Lazy(lazy_value)


# Generated at 2022-06-14 04:14:08.882236
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def get_value():
        return 1

    lazy = Validation.success(get_value).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.eval() == 1


# Generated at 2022-06-14 04:14:12.641703
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test suite for Validation#to_lazy method.
    """
    from pymonet.lazy import Lazy

    valid_validation = Validation(5, [])
    result = valid_validation.to_lazy()

    assert isinstance(result, Lazy)
    assert result() == 5


# Generated at 2022-06-14 04:14:18.741854
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    try:
        raise ValueError("Error")
    except ValueError as e:
        validation = Validation.fail([e])

    assert validation == validation.to_lazy().to_validation()

# Generated at 2022-06-14 04:14:22.164438
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    Validation.success(2).to_lazy() == Lazy(lambda: 2)
    Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:29.305664
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    # Test case when Validation has no errors
    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    # Test case when Validation has errors
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:34.922703
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    validation = Validation(1, [])
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.value() == Box(1)



# Generated at 2022-06-14 04:14:38.623882
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def some_func_for_lazy():
        return Validation(1, [])

    assert Lazy(some_func_for_lazy).to_lazy() == Validation(1, [])


# Generated at 2022-06-14 04:14:43.811582
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    s = Validation.success(lambda: Maybe.just(1))
    assert isinstance(s.to_lazy(), Lazy)

    f = Validation.fail(errors=[1, 2, 3])
    assert isinstance(f.to_lazy(), Lazy)



# Generated at 2022-06-14 04:14:51.259855
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad import is_monad, is_monad_instance
    from pymonet.monad import monad_laws

    def run(f):
        from pymonet.maybe import Maybe, Nothing
        from pymonet.monad import is_monad_instance

        if not is_monad_instance(f, Maybe):
            return f()

        return f.flat_map(lambda val: val.value)

    def f():
        return Validation.fail(['1', '2'])

    lazy = f().to_lazy()
    assert lazy == f()
    assert lazy.value == run(lazy.to_maybe())

    def g(i):
        return Validation.success(i)

    lazy = g(1).to_lazy()
    assert lazy == g(1)


# Generated at 2022-06-14 04:14:58.463129
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    # converts successful Validation to Lazy monad, where function as a value returns Validation value
    # this is test for function lazy_to_box
    assert Validation.success(0.0).to_lazy() == Lazy(lambda: 0.0)

    # converts failed Validation to Lazy monad, where function as a value returns Validation value
    # this is test for function lazy_to_box
    assert Validation.fail([0.0]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:15:02.717329
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.functions import pipeable
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    @pipeable
    def fn():
        return 1 / 0  # Generate exception


    @pipeable
    def monad_try_fn():
        return Try(1) / 0


    @pipeable
    def lazy_fn():
        return Lazy(lambda: Try(1)) / 0


    assert Validation(1, []).to_try() == Try(1)
    assert Validation(1, []).to_try().to_lazy() == Lazy(lambda: Try(1).to_lazy())
    assert Validation.fail([]).to_try().to_lazy() == Lazy(lambda: Try.fail().to_lazy())
   

# Generated at 2022-06-14 04:15:06.859615
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:17.712829
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    success_value = Validation.success(123)
    fail_value = Validation.fail(['error'])
    expected_value = Lazy(lambda: 123)
    expected_fail_value = Lazy(lambda: None)

    assert success_value.to_lazy() == expected_value
    assert fail_value.to_lazy() == expected_fail_value


# Generated at 2022-06-14 04:15:21.989930
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test box to lazy.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 42) == Validation.success(42).to_lazy()
    assert Lazy(lambda: None) == Validation.fail(['error']).to_lazy()


# Generated at 2022-06-14 04:15:25.028257
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    def get_value(value):
        return value

    def get_nothing():
        return None

    assert Validation.success(10).to_lazy() == Lazy(get_value, value=10)
    assert Validation.fail([10]).to_lazy() == Lazy(get_nothing)


# Generated at 2022-06-14 04:15:29.266900
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['Something went wrong']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:33.046805
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
  # Success validation
  validation = Validation.success(val=1)
  lazy = validation.to_lazy()
  assert lazy.value() == 1
  # Fail validation
  validation = Validation.fail(errors=[])
  lazy = validation.to_lazy()
  assert lazy.value() is None

# Generated at 2022-06-14 04:15:35.700300
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail(['E1', 'E2']).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:15:37.395799
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_result = Validation.success("ok").to_lazy()
    assert lazy_result == Lazy(lambda: "ok")


# Generated at 2022-06-14 04:15:39.223158
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given

    # When
    validation = Validation.success('Value')
    lazy_value = validation.to_lazy()

    # Then
    assert isinstance(lazy_value, Lazy)
    assert lazy_value() == 'Value'


# Generated at 2022-06-14 04:15:46.786726
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.monad_try import Try

    # Given
    try_monad: Try[str] = Try('Success')
    validation_monad: Validation[str, Exception] = Validation.success('Success')

    # When
    lazy_monad: Lazy[str] = validation_monad.to_lazy()

    # Then
    assert lazy_monad.unit() == Try.success('Success')


# Generated at 2022-06-14 04:15:52.015301
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given
    from pymonet.lazy import Lazy

    success_validation = Validation.success(3)
    fail_validation = Validation.fail()

    # When/Then
    assert success_validation.to_lazy() == Lazy(lambda: 3)
    assert fail_validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:01.150853
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test function doc
    """
    assert Validation.success("abc").to_lazy() == Lazy(lambda: "abc")  # successful Validation to_lazy == Lazy("abc")
    assert Validation.fail("error").to_lazy() == Lazy(lambda: None)  # failed Validation to_lazy == Lazy(None)


# Generated at 2022-06-14 04:16:05.306448
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    value = 'value'
    validation = Validation.success(value)

    lazy = validation.to_lazy()  # Lazy[Function() -> 'value']

    assert lazy == Lazy(lambda: value)

# Generated at 2022-06-14 04:16:12.774788
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    # when
    validation = Validation.success(1).to_lazy()
    validation_fail = Validation.fail([]).to_lazy()

    # then
    assert validation.value().call() == 1
    assert validation_fail.value().call() is None

    # and
    assert validation.map(lambda v: v + 1).call() == 2
    assert validation_fail.map(lambda v: v + 1).call() is None

    # and
    assert validation.bind(lambda v: Validation.success(v + 1)).call() == 2
    assert validation_fail.bind(lambda v: Validation.success(v + 1)).call() is None

# Generated at 2022-06-14 04:16:17.413957
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.fail(['error1', 'error2'])
    assert validation.to_lazy() == Lazy(lambda: None)

    validation = Validation.success(123)
    assert validation.to_lazy() == Lazy(lambda: 123)

# Generated at 2022-06-14 04:16:28.767151
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy method of Validation
    """
    from pymonet.lazy import Lazy
    import pytest

    lazy_value = Validation(None, []).to_lazy()
    assert isinstance(lazy_value, Lazy)

    defer_value = lazy_value.defer()
    assert defer_value is None

    lazy_value = Validation('value', []).to_lazy()
    defer_value = lazy_value.defer()
    assert defer_value == 'value'

    lazy_value = Validation('123', [InvalidNumber()]).to_lazy()
    with pytest.raises(InvalidNumberException):
        lazy_value.defer()


# Generated at 2022-06-14 04:16:36.286857
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    success_validation = Validation.success(5)
    assert success_validation.to_lazy() == Lazy(lambda: 5)

    failed_validation = Validation.fail('error')
    assert failed_validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:38.320028
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given
    validation = Validation.success(5)

    # When
    lazy = validation.to_lazy()

    # Then
    assert lazy.value() == 5


# Generated at 2022-06-14 04:16:43.660347
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:49.472585
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    v = Validation.success(1)
    l = v.to_lazy()
    assert l.get_value() == 1
    assert l.get_value() == 1
    assert isinstance(l, Lazy)
    v = Validation.fail(None)
    l = v.to_lazy()
    assert l.get_value() is None
    assert l.get_value() is None
    assert isinstance(l, Lazy)


# Generated at 2022-06-14 04:16:54.340777
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test should return non-empty list of Validations.
    """
    assert Validation.fail(['error']).to_lazy().unsafe_evaluate() == None
    assert Validation.success(['value']).to_lazy().unsafe_evaluate() == ['value']


# Generated at 2022-06-14 04:17:02.511201
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test case performs unit test for method to_lazy of class Validation
    """

    success = Validation.success(10)
    fail = Validation.fail()

    assert success.to_lazy() == Lazy(lambda: success.value)
    assert fail.to_lazy() == Lazy(lambda: fail.value)


# Generated at 2022-06-14 04:17:05.293954
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    lazy = validation.to_lazy()

    assert lazy == Lazy(lambda: 1)

# Generated at 2022-06-14 04:17:11.091753
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It converts Validation to Lazy monad.
    """
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    expected = Lazy(lambda: 10)
    actual = Validation.success(10).to_lazy()
    assert actual == expected

    expected = Lazy(lambda: None)
    actual = Validation.fail().to_lazy()
    assert actual == expected



# Generated at 2022-06-14 04:17:16.666310
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1), 'Validation.success(1).to_lazy() should return Lazy(lambda: 1)'
    assert Validation.fail(['Some error']).to_lazy() == Lazy(lambda: None), 'Validation.fail(["Some error"]).to_lazy() should return Lazy(lambda: None)'


# Generated at 2022-06-14 04:17:22.991751
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test case: when we have Validation with success value
    Expected: Lazy with successfully Try with value
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    m = Validation.success(1)
    assert m.to_lazy() == Lazy(lambda: 1)

    m = Validation.fail(1)
    assert m.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:26.283110
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def unsafe(message):
        raise Exception(message)

    validation = Validation.success(Lazy(lambda: unsafe('exception')))
    validation.to_lazy().value()



# Generated at 2022-06-14 04:17:27.799277
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()


# Generated at 2022-06-14 04:17:29.317432
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().force() == 1


# Generated at 2022-06-14 04:17:39.694572
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(1, ['Error']).to_lazy() == Lazy(lambda: 1)
    assert Validation(None, []).to_lazy() == Lazy(lambda: None)
    assert Validation(None, ['Error']).to_lazy() == Lazy(lambda: None)
    assert Validation(Try.success(1), []).to_lazy() == Lazy(lambda: Try.success(1))
    assert Validation(Try.success(1), ['Error']).to_lazy() == Lazy(lambda: Try.success(1))

# Generated at 2022-06-14 04:17:42.547478
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    val = Validation.success(1)
    assert val.to_lazy().value() == 1

    val = Validation.fail(['error1'])
    assert val.to_lazy().value() == None


# Generated at 2022-06-14 04:17:51.649650
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy = Validation.success(1).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 1

    lazy = Validation.success(1).to_lazy()

    assert lazy.get() == 1



# Generated at 2022-06-14 04:17:53.501895
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:17:57.785629
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def is_valid(value):
        errors = []
        if value > 10:
            errors.append('value is greater than 10')
        if value <= 0:
            errors.append('value is less or equal then 0')
        return Validation(value, errors)

    validation = is_valid(6)
    lazy = validation.to_lazy()

    assert lazy.value() == validation.value


# Generated at 2022-06-14 04:18:00.952841
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.fail(['e']).to_lazy() == Lazy(lambda: None)
    assert Validation.success('v').to_lazy() == Lazy(lambda: 'v')


# Generated at 2022-06-14 04:18:04.147598
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    f = Validation.success(lambda x: x * 2)

    assert f.to_lazy() == Lazy(lambda: lambda x: x * 2)


# Generated at 2022-06-14 04:18:08.086167
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    # WHEN
    lazy = Validation.success(1).to_lazy()

    # THEN
    assert Try(lazy.value()).is_success() is True
    assert lazy.value() == 1


# Generated at 2022-06-14 04:18:15.249919
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    success = Validation.success('success')
    assert success.to_lazy().value() == 'success'

    value = 1
    assert success.map(lambda v: Lazy.unit(v + 1)).bind(lambda x: Lazy.unit(x / 2)).value == 0.5

    lazy = Lazy.unit(value)
    assert lazy.bind(lambda x: success.map(lambda v: x + 1)).value() == 2

# Generated at 2022-06-14 04:18:22.024941
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It tests mapping on Validation class.
    """
    data = 'Test'
    v = Validation.success(data)
    l = v.to_lazy()
    assert l.evaluate() == data

    v = Validation.fail(['Error'])
    l = v.to_lazy()
    assert l.evaluate() == None


# Generated at 2022-06-14 04:18:24.055570
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()


# Generated at 2022-06-14 04:18:26.264487
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazyVal = Validation.success('test').to_lazy()
    assert lazyVal.get() == 'test'


# Generated at 2022-06-14 04:18:39.837108
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy().map(lambda x: x()).value == 1
    assert Validation.fail([]).to_lazy().map(lambda x: x()).is_fail() == True



# Generated at 2022-06-14 04:18:42.696356
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def get_value():
        return Validation.fail(['err1', 'err2'])

    lazy_result = Validation.fail(['err1', 'err2']).to_lazy()

    assert lazy_result.get() is None

# Generated at 2022-06-14 04:18:51.924464
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(12).to_lazy() == Lazy(lambda: 12)
    assert Validation.fail([12, 23]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:56.999060
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_value = Lazy(lambda: 2)
    lazy_box = Lazy(lambda: Validation.success(2))

    assert lazy_box.to_lazy() == lazy_value
    assert lazy_box.to_lazy().to_val().to_lazy() == lazy_value


# Generated at 2022-06-14 04:19:00.073339
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:19:05.664298
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    v1 = Validation.success(1)
    l1 = Lazy(lambda: 1)
    v2 = Validation.fail(['fail'])
    l2 = Lazy(lambda: None)

    assert v1.to_lazy() == l1
    assert v2.to_lazy() == l2

# Generated at 2022-06-14 04:19:09.250428
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    assert(isinstance(lazy, Lazy))
    assert(lazy() == 1)


# Generated at 2022-06-14 04:19:20.828745
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # test when validation is successful
    lazy = Validation.success("value").to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_successful() is True
    assert lazy.evaluate() == "value"
    assert lazy.value == "value"
    assert lazy.get_try().is_success() is True

    # test when validation is failed
    lazy = Validation.fail(["error"]).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_successful() is False
    assert lazy.value is None
    # if we evaluate lazy we will get exception, because it is failed lazy
    assert lazy.get_try().is_success() is False

# Generated at 2022-06-14 04:19:23.930095
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:19:29.182513
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.success(1).to_lazy()

    assert lazy.map(lambda x: x + 1).value == 2
    assert lazy.map(lambda x: x + 's').value == '1s'

# Generated at 2022-06-14 04:19:51.424263
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    val_success = Validation.success('value')
    val_fail = Validation.fail(['error'])

    assert val_success.to_lazy() == Lazy(lambda: 'value')
    assert val_fail.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:02.552990
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It should transform Validation to Lazy.

    :returns: Assertion
    :rtype: Assertion
    """
    from pymonet.monad_maybe import Maybe
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)

    # Function from pymonet.lazy import Lazy
    assert Validation.success(Maybe.nothing()).to_lazy().value == Lazy(lambda: Maybe.nothing())
    assert Validation.success(Maybe.just(10)).to_lazy().value == Lazy(lambda: Maybe.just(10))


# Generated at 2022-06-14 04:20:05.850316
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:09.034633
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It tests that Validation with value transformed to Lazy returns same value.
    """
    assert Validation.success(value=2).to_lazy().value() == 2


# Generated at 2022-06-14 04:20:14.138152
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def get_value():
        return "Validation test!"

    x = Validation.success(get_value)
    assert x.to_lazy().get() == "Validation test!"

    x = Validation.fail()
    assert x.to_lazy().get() is None

    def side_effect():
        raise ValueError("Error!")

    x = Validation.success(side_effect)
    assert x.to_lazy().get() is None

    x = Validation.fail()
    assert x.to_lazy().get() is None


# Generated at 2022-06-14 04:20:19.127261
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.success('str').to_lazy() == Lazy(lambda: 'str')


# Generated at 2022-06-14 04:20:24.065950
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    assert isinstance(Validation.success(0).to_lazy(), Lazy)
    assert Validation.success(0).to_lazy().evaluate() == 0
    assert isinstance(Validation.fail(0).to_lazy(), Lazy)
    assert Validation.fail(0).to_lazy().evaluate() == None


# Generated at 2022-06-14 04:20:27.735357
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.fail(['error']).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy != Lazy.of(None)


# Generated at 2022-06-14 04:20:32.827869
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    validation = Validation.success('hello world')

    assert validation == Lazy(lambda: 'hello world').to_validation()
    assert validation == Box('hello world').to_validation()
    assert validation == Lazy(lambda: Box('hello world')).to_validation().value.to_validation()
    assert validation == Box(Lazy(lambda: 'hello world')).to_validation().value.to_validation()

if __name__ == '__main__':  # pragma: no cover
    test_Validation_to_lazy()

# Generated at 2022-06-14 04:20:39.035776
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    success = Validation.success(5)
    assert success.to_lazy() == Lazy(lambda: 5)

    assert Validation.fail(['A']).to_lazy() != Lazy(lambda: None)
    assert success.to_lazy().value == 5
    assert success.to_lazy().is_ok() is True


# Generated at 2022-06-14 04:21:02.333039
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    val = Validation.success(1)
    assert val.to_lazy() == Lazy(lambda: val.value)



# Generated at 2022-06-14 04:21:08.205769
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    success = Validation.success()

    assert success.to_lazy() == Lazy(lambda: None)

    success = Validation.success(1)

    assert success.to_lazy() == Lazy(lambda: 1)

    fail = Validation.fail(['something wrong'])

    assert fail.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:21:15.526929
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.success(value='to_lazy val')
    assert validation.to_lazy() == Lazy(lambda: 'to_lazy val')

    validation = Validation.fail(errors=['error'])
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:21:17.775183
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.success(value=1).to_lazy()
    assert lazy.force() == 1

# Generated at 2022-06-14 04:21:22.801268
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.either import Right, Left
    from pymonet.lazy import Lazy

    lazy_val = Validation.success(1).to_lazy()
    assert isinstance(lazy_val, Lazy)
    assert lazy_val.value() == 1

    lazy_fail = Validation.fail([1, 2, 3]).to_lazy()
    assert isinstance(lazy_fail, Lazy)
    try:
        lazy_fail.value()
        assert False
    except:
        assert True

# Generated at 2022-06-14 04:21:26.241626
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    result = Validation.success('test').to_lazy()
    assert isinstance(result, Lazy)
    assert result.force() == 'test'
