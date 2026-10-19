

# Generated at 2022-06-14 04:11:35.677494
# Unit test for method to_maybe of class Validation
def test_Validation_to_maybe():  # pragma: no cover
    from pymonet.maybe import Maybe

    assert Validation.fail([]).to_maybe() == Maybe.nothing()
    assert Validation.fail(['err1']).to_maybe() == Maybe.nothing()

    assert Validation.success(1).to_maybe() == Maybe.just(1)
    assert Validation.success(1).to_maybe() == Maybe.just(1)


# Generated at 2022-06-14 04:11:39.921089
# Unit test for method to_maybe of class Validation
def test_Validation_to_maybe():
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    assert Validation.success(1).to_maybe() == Maybe.just(1)
    assert Validation.fail().to_maybe() == Maybe.nothing()


# Generated at 2022-06-14 04:11:43.499476
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:11:46.733946
# Unit test for method to_maybe of class Validation
def test_Validation_to_maybe():
    assert Validation.success(10).to_maybe().is_just()
    assert Validation.fail().to_maybe().is_nothing()

    assert Validation.success(10).to_maybe() == Maybe.just(10)
    assert Validation.fail().to_maybe() == Maybe.nothing()


# Generated at 2022-06-14 04:11:53.841559
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return "test"

    assert Validation.success().to_lazy() == Lazy(f)
    assert Validation(None, ['error']).to_lazy() == Lazy(f)
    assert Validation(1, ['error']).to_lazy() == Lazy(f)
    assert Validation('value', ['error']).to_lazy() == Lazy(f)


# Generated at 2022-06-14 04:11:56.228259
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(10)
    assert validation.to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 04:12:02.097447
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(Box(2)).to_lazy() == Lazy(lambda: Box(2))
    assert Validation.success(Try.success(3)).to_lazy() == Lazy(lambda: Try.success(3))



# Generated at 2022-06-14 04:12:05.346597
# Unit test for method to_maybe of class Validation
def test_Validation_to_maybe():
    from pymonet.maybe import Maybe

    value, errors = 'value', [1, 2, 3]

    success = Validation.success(value)
    assert success.to_maybe() == Maybe.just(value)

    fail = Validation.fail(errors)
    assert fail.to_maybe() == Maybe.nothing()


# Generated at 2022-06-14 04:12:09.534707
# Unit test for method to_maybe of class Validation
def test_Validation_to_maybe():
    """
    Unit test of method to_maybe of class Validation
    """
    # success validation
    validation = Validation.success('value')
    assert validation.to_maybe() == Maybe.just('value')

    # fail validation
    validation = Validation.fail(['error'])
    assert validation.to_maybe() == Maybe.nothing()



# Generated at 2022-06-14 04:12:14.571303
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_validation import Validation
    from pymonet.lazy import Lazy
    lazy = Validation.fail(['error 1', 'error 2']).to_lazy()
    assert lazy == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:22.650087
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""
    from pymonet.lazy import Lazy
    val: Validation = Validation.success(5)
    assert val.to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 04:12:25.382942
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().get() == 1
    assert Validation.fail(['error']).to_lazy().get() is None


# Generated at 2022-06-14 04:12:29.730202
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:12:31.463088
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail().to_lazy()


# Generated at 2022-06-14 04:12:34.574536
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    success = Validation.success(1)
    suc_lazy = success.to_lazy()
    assert suc_lazy.eval() == 1

    fail = Validation.fail()
    fail_lazy = fail.to_lazy()
    assert fail_lazy.eval() is None


# Generated at 2022-06-14 04:12:46.142179
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    ..  py:function:: test_Validation_to_lazy()

        Test method to_lazy of class Validation. When Validation is successful,
        lazy monad should return Validation value when value is called.
        In other case should returns nothing.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_identity import Identity

    # Test for successful Validation with value 'A'
    success_validation = Validation.success('A')
    lazy_result = success_validation.to_lazy()
    assert isinstance(lazy_result, Lazy)
    # Test for correct value
    assert Identity('A') == lazy_result.value()

    # Test for failed Validation
    failed_validation = Validation.fail(['A'])
    lazy_result

# Generated at 2022-06-14 04:12:48.732600
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Validation.success(10).to_lazy()


# Generated at 2022-06-14 04:12:55.368741
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    val = Validation(1, [])
    first = val.to_lazy()
    assert isinstance(first, Lazy), 'to_lazy should return an lazy monad'
    assert first.get_boxed() == 1, 'to_lazy should return an lazy monad wrapping value 1'
    second = val.to_try()
    assert isinstance(second, Try) and second.is_success(), 'to_try should return an success Try monad'

# Unit test of method bind

# Generated at 2022-06-14 04:12:59.883006
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:07.250036
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    from pymonet.monad_unit_tests.monad_test import monad_to_lazy_test

    assert monad_to_lazy_test(lambda a: Validation.success(a), Lazy, lambda a: a) == Validation.success(Lazy(lambda: a))
    assert monad_to_lazy_test(lambda a: Validation.fail(a), Lazy, lambda a: a) == Validation.fail(Lazy(lambda: a))



# Generated at 2022-06-14 04:13:14.997274
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:20.432360
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:28.971739
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_function():
        return "test"

    assert test_Validation_to_lazy.__name__ == 'test_Validation_to_lazy'
    assert Validation.success().to_lazy().value() == None
    assert Validation.success('Validation').to_lazy().value() == 'Validation'
    assert Validation.success(test_function).to_lazy().value() == test_function
    assert Validation.fail(['test']).to_lazy().value() == None

# Generated at 2022-06-14 04:13:31.040717
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    Validation.success(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 04:13:36.171954
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success("abc").to_lazy() == Lazy(lambda: "abc")
    assert Validation.fail("abc").to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:42.793663
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    lazy_try = Lazy(lambda: Try(1/0, is_success=True))
    assert lazy_try.get() == Try(1/0, is_success=True)
    assert lazy_try.get().value is not None
    assert Validation.success("123").to_lazy().get() == "123"
    assert lazy_try.get().to_lazy().get().is_success()



# Generated at 2022-06-14 04:13:50.160756
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """

    # Success case
    success_validation = Validation.success('success')
    lazy_success_validation = success_validation.to_lazy()
    assert lazy_success_validation.run() == 'success'

    # Fail case
    fail_validation = Validation.success('fail')
    lazy_fail_validation = fail_validation.to_lazy()
    assert lazy_fail_validation.run() is None



# Generated at 2022-06-14 04:13:53.138321
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.fail(errors=[100]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:56.495716
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def test_function():
        return 3

    assert Lazy(test_function) == Validation.success(3).to_lazy()


# Generated at 2022-06-14 04:14:01.269677
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    print('Test for method to_lazy of class Validation')
    validation = Validation(2, [])
    lazy_validation = validation.to_lazy()
    assert lazy_validation.value() == 2
    print('Test success')
    print('-----------------------------------')


# Generated at 2022-06-14 04:14:17.119501
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    success_val = Try(True)
    failure_val = Try(False)

    success_lazy = Lazy(lambda: True)
    failure_lazy = Lazy(lambda: False)

    assert success_val.to_lazy() == success_lazy
    assert failure_val.to_lazy() == failure_lazy



# Generated at 2022-06-14 04:14:21.083757
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail([3, 4]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:25.742032
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:33.519267
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    f = Validation.success(88).to_lazy()
    assert f is not None and f.is_function()
    assert f.get_value()() == 88
    assert f._value() == 88
    f = Validation.fail(['error']).to_lazy()
    assert f is not None and f.is_function()
    assert f.get_value()() is None
    assert f._value() is None


# Generated at 2022-06-14 04:14:38.107369
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    @Lazy
    def lazy_f():
        return 5

    validation = Validation.success(value=lazy_f())
    lazy = validation.to_lazy()

    assert validation.value() == lazy.value()

# Generated at 2022-06-14 04:14:39.673682
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.val import Validation
    from pymonet.lazy import Lazy

    assert Validation.success('fizz').to_lazy() == Lazy(lambda: 'fizz')
    Validation.fail().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:14:47.932372
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    try_ = Try(10)
    validation = Validation.success(12)
    lazy = validation.to_lazy()
    try:
        lazy.get()
    except:
        assert False
    try:
        validation.to_lazy().get()
    except:
        assert False
    try:
        try_.to_lazy().get()
    except:
        assert False
    try:
        Lazy(lambda: 20).get()
    except:
        assert False
    assert validation.to_lazy().get() == validation.value


# Generated at 2022-06-14 04:14:51.123343
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 1)
    assert Validation.success(1).to_lazy() == lazy


# Generated at 2022-06-14 04:14:59.151553
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    v = Validation.success('All ok')
    l = v.to_lazy()

    test_lazy = Lazy(lambda: 'Test lazy')
    assert l.value() == v.value

    e = Validation.fail(['First error', 'Second error'])
    l = e.to_lazy()

    assert l.value() == e.value

    t = Try(lambda: 'Hello', is_success=True)
    assert t == e.to_try()

# Generated at 2022-06-14 04:15:03.822990
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """

    validation = Validation.success(1)
    value = validation.to_lazy()

    assert value.is_defined()
    assert value.get() == 1


# Generated at 2022-06-14 04:15:26.722652
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation

    :returns: Nothing
    :rtype: Nothing
    """
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy().get_value() == 1
    assert Validation.fail([]).to_lazy().get_value() == None


# Generated at 2022-06-14 04:15:30.745336
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try, TryError
    from pymonet.lazy import Lazy
    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(2, [TryError('error')]).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 04:15:34.323555
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(4).to_lazy() == Lazy(lambda: 4)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:39.739637
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:42.510579
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('OK').to_lazy().evaluate() == 'OK'
    assert Validation.fail('ERROR').to_lazy().evaluate() is None


# Generated at 2022-06-14 04:15:46.058840
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:48.344888
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:50.153935
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    v = Validation.success()

    assert v.to_lazy().value() is None

# Generated at 2022-06-14 04:15:53.710658
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    @Lazy
    def create_validation():
        return Validation.success(1)

    assert create_validation().value == 1
    assert create_validation().to_lazy().value() == 1


# Generated at 2022-06-14 04:15:58.606448
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([2]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([2]) == Validation(None, [2])


# Generated at 2022-06-14 04:16:35.241670
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return 100

    val = Validation.success().map(f)
    assert val.to_lazy() == Lazy(f)

# Generated at 2022-06-14 04:16:37.715786
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(7).to_lazy() == Lazy(lambda: 7)


# Generated at 2022-06-14 04:16:45.750240
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def f():  # pragma: no cover
        return 42

    assert Validation.success(f).to_lazy() == Lazy(f)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:50.527277
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:53.623369
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_value = Lazy(lambda: 'value')
    validation = Validation('value', [])

    assert validation.to_lazy() == lazy_value

# Generated at 2022-06-14 04:16:57.582905
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1)
    validation = Validation.success(None)
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:02.010902
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(2).to_either() == Right(2)


# Generated at 2022-06-14 04:17:12.156748
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)
    assert Validation.success([]).to_lazy() == Lazy(lambda: [])
    assert Validation.success([1]).to_lazy() == Lazy(lambda: [1])
    assert Validation.success([1, 2]).to_lazy() == Lazy(lambda: [1, 2])


# Generated at 2022-06-14 04:17:18.472169
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    # Happy path
    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1)

    # Fail
    validation = Validation.fail(['some error'])
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:20.778355
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validate_unit_test_for('test_Validation', 'to_lazy', ['value'], [42], Validation.success(42).to_lazy().evaluate)



# Generated at 2022-06-14 04:18:37.983249
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Tests for successful validation
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)

    # Tests for failed validation
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:18:41.958646
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    def fn(p):
        return p + 1
    assert Validation.success(1).to_lazy() == Lazy(fn, 1)
    assert Validation.fail([1,2]).to_lazy() == Lazy(fn, 1)


# Generated at 2022-06-14 04:18:45.837738
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(lambda: 1)

    def dummy_function():
        return None

    validation = Validation.success(dummy_function)
    assert validation.to_lazy().get() == dummy_function()



# Generated at 2022-06-14 04:18:52.032870
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_try import _Try
    from pymonet.lazy import Lazy

    t = Lazy(lambda: 'Some value')
    v = Validation.success(t).to_lazy()
    if not isinstance(v, Lazy):
        return False
    if not v.evaluate() == 'Some value':
        return False


# Generated at 2022-06-14 04:18:55.571065
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:18:57.933476
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success('a')
    lazy_val = validation.to_lazy()
    assert validation == lazy_val.value


# Generated at 2022-06-14 04:19:00.402881
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail(3).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:10.653133
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import Monad
    from pymonet.validation import Validation
    from pymonet.functor import Functor

    validation_monad = Validation.success(1)
    assert isinstance(validation_monad.to_lazy(), Monad)
    assert isinstance(validation_monad.to_lazy(), Functor)

    lazy_monad = validation_monad.to_lazy()
    assert isinstance(lazy_monad, Monad)
    assert isinstance(lazy_monad, Functor)
    assert lazy_monad.value() == 1

    test_lazy_validation = Validation.fail(None)
    assert test_lazy_validation.to_lazy().value() == None

# Generated at 2022-06-14 04:19:22.977587
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    def some_func(x):
        return x ** x

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(2, [5]).to_lazy() == Lazy(lambda: 2)
    assert Validation(3, []).to_lazy().bind(some_func) == Lazy(lambda: 27)
    assert Validation(7, [10]).to_lazy().bind(some_func) == Lazy(lambda: 823543)
    assert Validation(4, [1, 3, 5]).to_lazy().ap(Lazy(lambda x: Validation(x + 2, [x ** 2]))) == Lazy(lambda: 6)
    assert Val

# Generated at 2022-06-14 04:19:27.607225
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    assert Validation.success(4).to_lazy() == Lazy(lambda: 4)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:48.797161
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    result = Validation.success(value=1).to_lazy().eval()
    assert result == 1



# Generated at 2022-06-14 04:20:51.968782
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([3, 2, 1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:21:00.118253
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def _to_lazy(x):
        return Lazy(lambda: x)

    assert Validation.success(1).map(_to_lazy) == Lazy(lambda: 1)
    assert Validation.fail([1]).map(_to_lazy) == Lazy(lambda: None)

# # Unit test for method to_try of class Validation

# Generated at 2022-06-14 04:21:04.875662
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.validation import Validation

    assert Lazy(3) == Validation.success(3).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([3]).to_lazy()
    return


# Generated at 2022-06-14 04:21:10.736317
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.monad_identity import Identity
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy() == Lazy(lambda: Identity(1).value)
    assert Validation.success(1).to_lazy() == Lazy(lambda: Success(1).value)
    assert Validation.success(1).to_lazy() == Lazy(lambda: Try(1, True).value)


# Generated at 2022-06-14 04:21:18.222446
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # given
    from pymonet import monad_try as mt

    # when
    try_val1 = Validation.success("value").to_lazy()
    try_val2 = Validation.fail("error").to_lazy()

    # then
    assert (mt.Try.success("value") == try_val1.value())
    assert (mt.Try.fail("error") == try_val2.value())


# Generated at 2022-06-14 04:21:21.491820
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    lazy = Lazy(lambda: 1)
    assert validation.to_lazy() == lazy
    assert validation.to_lazy().force() == lazy.force()



# Generated at 2022-06-14 04:21:26.617018
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    def get_result():
        return Validation.success('result')

    assert Validation.success('result').to_lazy() == Lazy(get_result)

