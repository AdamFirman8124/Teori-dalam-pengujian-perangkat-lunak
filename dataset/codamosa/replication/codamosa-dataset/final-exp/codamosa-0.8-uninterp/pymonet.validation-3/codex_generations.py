

# Generated at 2022-06-14 04:11:38.643700
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def no_operation():
        return False

    def success():
        return Validation.success(1)

    def fail():
        return Validation.fail([1, 2, 3])

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)

    assert success().to_lazy().value == 1
    assert fail().to_lazy().value is None

    assert success().to_lazy().is_success()
    assert not fail().to_lazy().is_success()

    assert success().to_lazy().is_fail()
    assert not fail().to_lazy().is_fail()

# Generated at 2022-06-14 04:11:42.262141
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Failure

    m = Validation.fail(['Error message'])
    m_to_lazy = m.to_lazy()
    assert m_to_lazy.value() is None and m_to_lazy.is_success() is False

# Generated at 2022-06-14 04:11:45.704855
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Lazy(lambda: None) == Validation.fail().to_lazy()
    assert Lazy(lambda: 'value') == Validation.success('value').to_lazy()



# Generated at 2022-06-14 04:11:52.209316
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(2).to_lazy() == \
           Lazy(lambda: 2)

    assert Validation.success(None).to_lazy() == \
           Lazy(lambda: None)

    assert Validation.fail(["error"]).to_lazy() == \
           Lazy(lambda: None)


# Generated at 2022-06-14 04:12:01.825373
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    a = Validation.success(7)\
        .to_lazy()\
        .map(lambda x: Validation.success(x + 1).to_lazy())\
        .flat_map(lambda x: x.map(lambda y: Validation.success(y + 2).to_lazy()))\
        .flat_map(lambda x: x.map(lambda y: y**2))

    assert a.value() == 64

    # An exception must be raised
    try:
        a = Validation.fail(['error']).to_lazy()
        raise ValueError('An exception must be raised')
    except Exception as e:
        assert type(e) == TypeError
        assert str(e) == 'Lazy: evaluation contains errors.'

    # result equal to 2
    a = Validation.success(1).to

# Generated at 2022-06-14 04:12:06.747194
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation_just = Validation.success(100)
    assert validation_just.to_lazy() == Lazy(lambda: 100)

    validation_nothing = Validation.fail()
    assert validation_nothing.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:08.274789
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(1)
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.value() == 1


# Generated at 2022-06-14 04:12:13.131260
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success('data')
    lazy = validation.to_lazy()
    assert lazy.eval() == 'data'

    validation = Validation.fail()
    lazy = validation.to_lazy()
    assert lazy.eval() is None


# Generated at 2022-06-14 04:12:17.657430
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(None, ['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:23.050434
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success('aaa').to_lazy() == Lazy(lambda: 'aaa')
    assert Validation.fail(['aaa']).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:12:29.218126
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert (Validation.success(100).to_lazy() == Lazy(lambda: 100))
    assert (Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None))


# Generated at 2022-06-14 04:12:36.393970
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from unittest import TestCase, main

    from pymonet.monad_try import Try

    from pymonet.lazy import Lazy

    from pymonet.box import Box

    from pymonet.either import Left, Right

    from pymonet.maybe import Maybe

    from pymonet.validation import Validation

    class ValidationTest(TestCase):
        """
        Test for Validation class.
        """

        def test_to_lazy(self):
            """
            Test for Validation to lazy conversion.

            Validation.success(value) => Lazy(value)
            Validation.fail(errors) => Lazy(None)
            """
            value = 'test'
            errors = ['error']

            self

# Generated at 2022-06-14 04:12:42.012348
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.success(3).to_lazy().eval() == 3
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.fail().to_lazy().eval() is None



# Generated at 2022-06-14 04:12:49.161834
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.success([1, 2, 3])
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get_value() == [1, 2, 3]

    validation = Validation.fail([1, 2, 3])
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert Try(lazy.get_value(), is_success=False) == Try(None, is_success=False)



# Generated at 2022-06-14 04:12:52.636845
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 2)

    val = Validation.success(2)
    assert val.to_lazy() == lazy

    val = Validation.fail(['error'])
    assert val.to_lazy() == lazy


# Generated at 2022-06-14 04:13:02.486592
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation('1', []) == Validation.success().to_lazy().flat_map(
        lambda x: Try(x * 2) if x is not None else Try(None, is_success=False)
    ).to_validation()

    assert Validation(None, []) == Validation.fail().to_lazy()

    assert Lazy(lambda: 10) == Validation.success(10).to_lazy()



# Generated at 2022-06-14 04:13:05.198550
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(3).to_lazy().get() == 3
    assert Validation.fail(3).to_lazy().get() == None


# Generated at 2022-06-14 04:13:08.477809
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.success('value')
    assert validation.to_lazy() == Lazy(lambda: 'value')
    assert validation.to_lazy().f() == 'value'


# Generated at 2022-06-14 04:13:11.119004
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 2

    assert Validation.success(func).to_lazy() == Lazy(func)

# Generated at 2022-06-14 04:13:15.961516
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda:1)
    assert Validation.success(None).to_lazy() == Lazy(lambda:None)
    assert Validation.fail([]).to_lazy() == Lazy(lambda:None)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda:None)


# Generated at 2022-06-14 04:13:21.309690
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 04:13:27.642654
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.fail(errors=['error']).to_lazy() == Lazy(lambda: 'error')
    assert Validation.success(value='value').to_lazy() == Lazy(lambda: 'value')


# Generated at 2022-06-14 04:13:32.466895
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy().take() == 1
    assert Validation.success(1).to_lazy().take() == 1



# Generated at 2022-06-14 04:13:36.727550
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.option import Option

    no_errors = Validation.success(1)
    errors = Validation.fail(['Error1', 'Error2'])

    # must returns Callable monad wrapped in Lazy Monad
    assert no_errors.to_lazy() == Lazy(no_errors.value)
    assert errors.to_lazy() == Lazy(errors.value)



# Generated at 2022-06-14 04:13:44.328493
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_validation = Validation.success([1, 2, 3]).to_lazy()
    assert lazy_validation == Lazy(lambda: [1, 2, 3])
    assert lazy_validation() == [1, 2, 3]

    lazy_validation = Validation.success(1).to_lazy()
    assert lazy_validation == Lazy(lambda: 1)
    assert lazy_validation() == 1

    lazy_validation = Validation.fail([1, 2, 3]).to_lazy()
    assert lazy_validation == Lazy(lambda: None)
    assert lazy_validation() is None


# Generated at 2022-06-14 04:13:48.934038
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    def assert_value(value_lazy):
        assert value_lazy == 'Value'

    validation = Validation('Value', [])
    validation.to_lazy().consume(assert_value)


# Generated at 2022-06-14 04:13:53.755689
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    result = validation.to_lazy()
    assert result == Lazy(lambda: 1)

    validation = Validation.fail()
    result = validation.to_lazy()
    assert result == Lazy(lambda: None)

test_Validation_to_lazy()



# Generated at 2022-06-14 04:13:57.357321
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    value = 1
    r = Validation.success(value)
    assert Lazy.unit(value) == r.to_lazy()


# Generated at 2022-06-14 04:14:01.016978
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    validation = Validation(value=1, errors=[])
    assert (validation.to_lazy() == Lazy(lambda: 1))


# Generated at 2022-06-14 04:14:07.382667
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    value = Lazy(lambda: 'value')
    assert Validation.success(value).to_lazy() == Lazy(lambda: value)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:14:20.701960
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def test_func():
        return 'test'

    assert Validation.success(test_func).to_lazy() == Lazy(test_func)
    assert Validation.fail(test_func).to_lazy() == Lazy(None)
    assert Validation.success().to_lazy() == Lazy(None)
    assert Validation.fail().to_lazy() == Lazy(None)


# Generated at 2022-06-14 04:14:24.374343
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    f = lambda x: x + 2
    validation = Validation.success(1).map(f)

    assert validation.to_lazy() == Lazy(lambda: validation.value)


# Generated at 2022-06-14 04:14:26.943354
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')


# Generated at 2022-06-14 04:14:32.734312
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def call_me():
        return 'Successful Validation'

    validation_success = Validation.success(call_me)
    assert validation_success.to_lazy().evaluate() == 'Successful Validation'

    validation_failure = Validation('Error', [])
    assert validation_failure.to_lazy().evaluate() == None



# Generated at 2022-06-14 04:14:41.332426
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(42)
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy), 'to_lazy returns Lazy'
    assert lazy.get() == 42, 'lazy get return 42'

    validation = Validation.fail('error')
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy), 'to_lazy returns Lazy'
    assert lazy.get() is None, 'lazy get return None'


# Generated at 2022-06-14 04:14:44.861235
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return Validation.success(1)

    lazy = Lazy(func)

    assert (Validation.success(1) == lazy.get())


# Generated at 2022-06-14 04:14:48.887153
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().unsafe_perform() == 1

    assert Validation.fail([1]).to_lazy().unsafe_perform() == None


# Generated at 2022-06-14 04:14:51.265621
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.success(1).to_lazy()
    assert lazy.get() == 1

# Generated at 2022-06-14 04:14:57.246364
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy_success = Validation.success(2).to_lazy()
    assert lazy_success == Lazy(lambda: 2)

    lazy_fail = Validation.fail([2]).to_lazy()
    assert lazy_fail == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:00.561603
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    success = Validation.success(1)
    assert success.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 04:15:10.484621
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(42).to_lazy().get_value() == 42
    assert Validation.fail().to_lazy().get_value() is None


# Generated at 2022-06-14 04:15:15.280459
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.validation import Validation

    def call():
        return 'value'

    assert Validation.success().to_lazy().call() == 'value'
    assert Validation.fail().to_lazy().is_success() == False


# Generated at 2022-06-14 04:15:18.265352
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    v = Validation.success(1)
    assert v.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:15:24.007893
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.success('hello').to_lazy() == Lazy(lambda: 'hello')
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:26.534394
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(1)

    assert validation.to_lazy().get() == 1

# Generated at 2022-06-14 04:15:32.212413
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from nose.tools import assert_equal
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    # Test for lazy with Validation success
    val = Validation.success({'name': 'pymonet'})
    lzy = val.to_lazy()
    assert_equal(isinstance(lzy, Lazy), True)
    assert_equal(lzy.get(), val.value)

    # Test for lazy with Validation fail
    val = Validation.fail(['error message'])
    lzy = val.to_lazy()
    assert_equal(isinstance(lzy, Lazy), True)
    assert_equal(lzy.get(), val.value)


# Generated at 2022-06-14 04:15:35.444475
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 04:15:39.783782
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    v = Validation.success(Lazy(lambda: 1))

    assert v.to_lazy() == Lazy(lambda: Lazy(lambda: 1))
    assert v.to_lazy().value() == Lazy(lambda: 1)

# Generated at 2022-06-14 04:15:44.982194
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success().to_lazy() == Lazy(lambda: None)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:15:55.378073
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    validation = Validation.fail(['error']).to_lazy()
    assert isinstance(validation, Lazy)
    assert isinstance(validation.get(), Try)
    assert validation.get().is_fail() is False
    assert validation.get().is_success() is False
    assert validation.get().value is None

    validation = Validation.success('value').to_lazy()
    assert isinstance(validation, Lazy)
    assert isinstance(validation.get(), Try)
    assert validation.get().is_fail() is False
    assert validation.get().value == 'value'
    assert validation.get().is_success() is True


# Generated at 2022-06-14 04:16:05.793143
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    assert Try.success(2).to_lazy().eval() == 2
    assert Try.fail([]).to_lazy().eval() is None

# Generated at 2022-06-14 04:16:09.648702
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation to_lazy method returns Lazy object with Validation value.
    """
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([5]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:16:20.419562
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success("A").to_lazy() == Lazy("A")
    assert Validation.success("A").map(lambda a: a + "B").to_lazy() == Lazy("AB")
    assert Validation.success("A").bind(lambda a: Validation.success(a + "B")).to_lazy() == Lazy("AB")
    assert Validation.success("A").to_lazy().map(lambda a: a + "B") == Lazy("AB")
    assert Validation.success("A").ap(lambda a: Validation.success(a + "B")).to_lazy() == Lazy("B")
    assert Validation.success("A").to_lazy().ap(lambda a: Validation.success(a + "B")) == Lazy("B")

    assert Validation.fail

# Generated at 2022-06-14 04:16:23.700325
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('hello').to_lazy().get() == 'hello'


# Generated at 2022-06-14 04:16:32.790167
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    # check that result is a Lazy monad
    assert (Validation.success(True).to_lazy() == Lazy(lambda: True))

    # check errors are not omitted
    assert (Validation.fail([ValueError('Test')]).to_lazy().value() == None)

    # check that to_lazy is the inverse of to_try
    assert (Validation.success(1).to_lazy() == Validation.success(1).to_try().to_lazy())
    assert (Validation.fail([ValueError('Failed')]).to_lazy() == Try(None, is_success=False).to_lazy())



# Generated at 2022-06-14 04:16:42.120714
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try


    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)

    def func():
        raise Exception()
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)

    try:
        Validation.fail([1]).to_lazy().value()
        assert False
    except Exception:
        assert True


# Generated at 2022-06-14 04:16:50.798389
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def test_fn():
        return 'test'

    validation = Lazy(test_fn).to_validation()
    assert validation == Validation('test', [])
    lazy = validation.to_lazy()
    assert lazy == Lazy(test_fn)

    validation = Try(test_fn).to_validation()
    assert validation == Validation('test', [])
    lazy = validation.to_lazy()
    assert lazy == Lazy(test_fn)

    validation = Lazy(test_fn).to_validation()
    assert validation == Validation('test', [])
    lazy = validation.to_lazy()
    assert lazy == Lazy(test_fn)


# Generated at 2022-06-14 04:16:53.917161
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:01.972429
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def fn(value):
        return Lazy(lambda: value)

    result = Validation.success(10).to_lazy()
    assert isinstance(result, Lazy)
    assert callable(result.value)
    assert result.value() == 10
    assert result == fn(10)
    assert str(result) == "Lazy[<function Validation_to_lazy.<locals>.<lambda> at 0x7f0a2d2e1bf8>]"


# Unit tests for method to_try of class Validation

# Generated at 2022-06-14 04:17:06.134856
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Test 1. When Validation is successful
    assert Lazy(10) == Validation.success(10).to_lazy()

    # Test 2. When Validation is failed
    assert Lazy(None) == Validation.fail().to_lazy()


# Generated at 2022-06-14 04:17:20.362892
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.success(0).to_lazy() == Lazy(lambda: 0)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:24.587464
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): #pragma: no cover
    from pymonet.lazy import Lazy

    result = Validation.success().to_lazy()

    assert isinstance(result, Lazy)
    assert result.value() is None


# Generated at 2022-06-14 04:17:28.668933
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def function_to_test():
        return 3

    result = Validation.success(function_to_test()).to_lazy()

    assert(isinstance(result, Lazy))
    assert(3 == result.get())


# Generated at 2022-06-14 04:17:33.573836
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_function():
        return 'Value'

    def test_function2():
        raise Exception('Exception')

    assert Validation.success('Value').to_lazy() == Lazy(test_function)
    assert Validation.fail(errors=[]).to_lazy() == Lazy(test_function2)


# Generated at 2022-06-14 04:17:38.431548
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given
    validation = Validation.fail()

    # When
    result = validation.to_lazy()

    # Then
    assert result.is_lazy() and result.is_fail()

    # When
    result = result.force()

    # Then
    assert not result.is_lazy() and result.is_fail()


# Generated at 2022-06-14 04:17:41.325802
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def get_data():
        return Validation.success(1)

    result = get_data().to_lazy()

    assert result == Lazy(get_data)



# Generated at 2022-06-14 04:17:46.752415
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    # Given
    success = Validation.success(42)
    fail = Validation.fail(['error'])

    # When
    lazy_success = success.to_lazy()
    lazy_fail = fail.to_lazy()

    # Then
    assert(lazy_success == Lazy(lambda: 42))
    assert(lazy_fail == Lazy(lambda: None))

# Generated at 2022-06-14 04:17:51.512081
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == \
        Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == \
        Lazy(lambda: None)


# Generated at 2022-06-14 04:17:59.806252
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def lazy_function():
        return 1

    # Success
    assert Validation.success(1).to_lazy() == Lazy(lazy_function)
    assert Validation.success(1).to_lazy() == Lazy(lazy_function)
    assert Validation.success(1).to_lazy() == Lazy(lazy_function)
    assert Validation.success(1).to_lazy().get() == 1

    # Failure
    assert Validation.fail().to_lazy() == Lazy(lazy_function)
    assert Validation.fail().to_lazy() == Lazy(lazy_function)
    assert Validation.fail().to_lazy() == Lazy(lazy_function)
    assert Validation.fail().to_lazy().get() is None


# Generated at 2022-06-14 04:18:05.825682
# Unit test for method to_lazy of class Validation

# Generated at 2022-06-14 04:18:25.069962
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    a = Maybe.just(5)
    b = Maybe.nothing()
    c = Maybe.from_nullable(None)
    d = Maybe.from_nullable(5)
    assert a.to_lazy() == Lazy(lambda: Maybe.just(5))
    assert b.to_lazy() == Lazy(lambda: Maybe.nothing())
    assert c.to_lazy() == Lazy(lambda: Maybe. from_nullable(None))
    assert d.to_lazy() == Lazy(lambda: Maybe.from_nullable(5))


# Generated at 2022-06-14 04:18:31.292439
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.fail(['error'])
    lazy = validation.to_lazy()
    assert lazy.f == None
    assert lazy.eval() == None

    validation = Validation.success('success')
    lazy = validation.to_lazy()
    assert lazy.f == None
    assert lazy.eval() == 'success'



# Generated at 2022-06-14 04:18:38.641053
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """Test for method to_lazy of class Validation"""
    from pymonet.lazy import Lazy

    # when validations is successful
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.success(5).to_lazy().value() == 5

    # when validations is not successful
    assert Validation.fail(['some error']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['some error']).to_lazy().value() is None


# Generated at 2022-06-14 04:18:41.508381
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_mapper(x):
        return x

    assert Validation.success(10).to_lazy().map(test_mapper) == Lazy(lambda: 10)


# Generated at 2022-06-14 04:18:43.345802
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(10)
    lazy = validation.to_lazy()
    assert lazy.eval() == validation.value


# Generated at 2022-06-14 04:18:50.044236
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for to_try of class Validation"""
    success_validation = Validation.success(42)
    assert success_validation.to_lazy().get() == 42

    fail_validation = Validation.fail(['error'])
    assert fail_validation.to_lazy().get() == None


# Generated at 2022-06-14 04:18:53.149801
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:58.076263
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([42]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:19:00.820367
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(5).to_lazy()

    assert lazy is not None
    assert isinstance(lazy, Lazy)

    assert lazy.get() == 5


# Generated at 2022-06-14 04:19:04.225281
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.fail() == Validation.fail().to_lazy().get()
    assert Validation.success(2) == Validation.success(2).to_lazy().get()


# Generated at 2022-06-14 04:19:17.465744
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy().evaluate() == 5
    assert Validation.fail().to_lazy().evaluate() is None


# Generated at 2022-06-14 04:19:21.896273
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """

    from pymonet.lazy import Lazy

    result = Validation.success(1).to_lazy()
    assert result == Lazy(lambda: 1)

    result = Validation.fail(1).to_lazy()
    assert result == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:32.077021
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test unit test for method to_lazy of class Validation."""
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.validation import Validation
    from pymonet.validation import Validation
    from pymonet.validation import Validation
    from pymonet.validation import Validation
    from pymonet.validation import Validation
    from pymonet.validation import Validation

    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:35.893722
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(44).to_lazy().eval() == 44
    assert Validation.fail(['error']).to_lazy().eval() is None


# Generated at 2022-06-14 04:19:44.435705
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(["Error"]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(2).map(lambda a: Try(a, True)).to_lazy() == Lazy(lambda: Try(2, True))
    assert Validation.fail(["Error"]).map(lambda a: Try(a, False)).to_lazy() == Lazy(lambda: Try(None, is_success=False))


# Generated at 2022-06-14 04:19:49.251533
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:52.189920
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """Unit test for method to_lazy of class Validation"""

    from pymonet.lazy import Lazy

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:57.357093
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:01.843539
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation.to_lazy() should transform Validation to Lazy monad.
    """
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    lazy = validation.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.force() == 1


# Generated at 2022-06-14 04:20:05.543373
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    some_value = 'someValue'
    validation = Validation.success(some_value)

    def call_me():
        return some_value
    assert validation.to_lazy() == Lazy(call_me)


# Generated at 2022-06-14 04:20:23.875162
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    result_1 = Lazy.unit(Validation.success(1)) \
                    .ap(lambda v: Lazy.unit(Validation.success(v + 1))) \
                    .ap(lambda v: Lazy.unit(Validation.success(v + 2))) \
                    .to_lazy()

    result_2 = Lazy.unit(Validation.success(1)) \
                    .ap(lambda v: Lazy.unit(Validation.fail(['error']))) \
                    .ap(lambda v: Lazy.unit(Validation.success(v + 2))) \
                    .to_lazy()

    assert result_1.eval() == Validation.success(4)
    assert result_2.eval() == Validation.fail(['error'])

# Generated at 2022-06-14 04:20:26.919232
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('A').to_lazy() == Lazy(lambda: 'A')


# Generated at 2022-06-14 04:20:29.086941
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    x = Validation.success(10)
    assert x.to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 04:20:37.268314
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation_success = Validation.success(10)
    assert validation_success.to_lazy() == Lazy(lambda: 10)

    validation_fail = Validation.fail(errors=['error'])
    assert validation_fail.to_lazy() == Lazy(lambda: None)

    try_success = Try(5)
    assert validation_success.to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 04:20:42.609682
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:48.243319
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation('value', [1, 2]).to_lazy() == Lazy(lambda: 'value')
    assert Validation(1, []).to_try() == Try(1, is_success=True)



# Generated at 2022-06-14 04:20:52.677657
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # Given: Validation successful
    validation = Validation.fail([1, 2]).to_lazy()

    # When: call method to_lazy of class Validation
    result = validation.to_lazy()

    # Then: returns Lazy monad with function returning Validation value
    assert(isinstance(result, Lazy))
    assert(result.eval() == [1, 2])


# Generated at 2022-06-14 04:21:01.618212
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    value = 'value'
    assert Validation.success(value).to_lazy() == Lazy(lambda: value)
    assert Validation.fail(['critical error']).to_lazy() == Lazy(lambda: None)
    assert Validation.success().to_lazy() == Lazy(lambda: None)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:21:03.252674
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 04:21:07.184947
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    value = 'text'
    validation = Validation.success(value)
    lazy = validation.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == value


# Generated at 2022-06-14 04:21:21.493532
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.test_utils import get_test_value, get_test_container
    from pymonet.lazy import Lazy

    value = get_test_value()

    validation = Validation.success(value)
    lazy = validation.to_lazy()
    assert lazy == Lazy(lambda: value)


# Generated at 2022-06-14 04:21:23.658711
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('hello').to_lazy().run() == 'hello'


# Generated at 2022-06-14 04:21:32.114494
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Assert that Validation().to_lazy() returns expected value.
    :return:
    """
    from typing import Any

    from pymonet.monad_try import Try

    from pymonet.lazy import Lazy
