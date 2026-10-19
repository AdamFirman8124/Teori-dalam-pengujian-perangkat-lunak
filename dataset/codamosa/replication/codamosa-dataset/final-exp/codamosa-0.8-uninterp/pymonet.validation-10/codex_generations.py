

# Generated at 2022-06-14 04:11:37.531964
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    def success_func():
        return 'success'

    def fail_func():
        raise Exception('error')

    assert Validation.success('success').to_lazy().value() == 'success'
    assert Validation.success(success_func).to_lazy().value() == 'success'
    assert Validation.fail(['error']).to_lazy().value() is None
    assert Validation.fail([fail_func]).to_lazy().value() is None
    assert Validation.fail([fail_func]).to_lazy().get_error() == ['error']

# Generated at 2022-06-14 04:11:41.677528
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Try.success(1).to_lazy() == Lazy(lambda: 1)
    assert Try.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:11:48.865855
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_success_func():
        return Validation.success(10)

    def lazy_fail_func():
        return Validation.fail(['error1'])

    validation_success = Validation.success(10)
    validation_fail = Validation.fail(['error1'])

    assert validation_success.to_lazy() == Lazy(lazy_success_func)
    assert validation_fail.to_lazy() == Lazy(lazy_fail_func)


# Generated at 2022-06-14 04:11:55.474729
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import Monad

    def test(value):
        def func_to_lazy(validation):
            return validation.to_lazy()

        lazy = func_to_lazy(value)

        return lazy.is_instance(Lazy) and \
               lazy.eval() == Monad.defalt_value(value)

    assert test(Validation.success(1))
    assert test(Validation.fail(1))


# Generated at 2022-06-14 04:11:58.392924
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def _test(expected, actual):
        assert expected == actual
    validation = Validation(5, [])
    _test(5, validation.to_lazy().eval())



# Generated at 2022-06-14 04:12:03.682460
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Function tests Validation.to_lazy method.

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['haha']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:09.193380
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_validation import Validation
    from pymonet.lazy import Lazy

    def test_fn(param):
        if param >= 0:
            return Validation.success(param)
        return Validation.fail([param])

    assert test_fn(-1000).to_lazy() == Lazy(lambda: -1000)
    assert test_fn(1000).to_lazy() == Lazy(lambda: 1000)


# Generated at 2022-06-14 04:12:15.917942
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['a']).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:12:20.095329
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('test').to_lazy().value() == 'test'
    assert Validation.fail(['test']).to_lazy().value() is None



# Generated at 2022-06-14 04:12:24.948289
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    success = Validation.success('success')
    assert success.to_lazy() == Lazy(lambda: 'success')

    fail = Validation.fail(['error'])
    assert fail.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:12:28.726719
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(5)


# Generated at 2022-06-14 04:12:30.980699
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    value = Validation.success(True).to_lazy()

    assert value.value()


# Generated at 2022-06-14 04:12:35.650613
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')


# Generated at 2022-06-14 04:12:39.659984
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(42).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.run() == 42


# Generated at 2022-06-14 04:12:44.384614
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy method of Validation class
    """
    from pymonet.lazy import Lazy

    validation = Validation.success(2)
    assert validation == validation.to_lazy().force()
    assert validation != validation.to_lazy()
    assert validation != Lazy(lambda: 2)


# Generated at 2022-06-14 04:12:47.737754
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 04:12:51.663451
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(12).to_lazy() == Lazy(lambda: 12)
    assert Validation.fail(12).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:57.810488
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('a').to_lazy() == Lazy(lambda: 'a')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['a']).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:13:06.680838
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy.
    """
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    validation = Validation.success(5)
    assert validation.to_lazy() == Lazy(lambda: 5)
    assert validation.to_lazy().unsafe_run() == 5

    validation = Validation.fail([1, 2, 3])
    assert validation.to_lazy() == Lazy(lambda: None)
    assert validation.to_lazy().unsafe_run() is None



# Generated at 2022-06-14 04:13:09.986055
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def lazy_function():
        return 'test'
    validation = Validation.success(lazy_function)
    lazy = validation.to_lazy()
    assert lazy.value() == lazy_function()



# Generated at 2022-06-14 04:13:13.985795
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test for method to_lazy of class Validation.
    """
    validation = Validation.success(9)
    assert validation.to_lazy().get() == 9


# Generated at 2022-06-14 04:13:16.519492
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(2).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == 2


# Generated at 2022-06-14 04:13:22.856104
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_lazy import Lazy

    fn = lambda: 'value'
    lazy = Lazy(fn)
    assert lazy.get() == 'value'
    assert lazy.value == 'value'
    assert lazy.access() == 'value'
    assert lazy.get_or_raise(RuntimeError) == 'value'

# Generated at 2022-06-14 04:13:28.222416
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(10, []).to_lazy() == Lazy(lambda: 10)
    assert Validation('test', []).to_lazy() == Lazy(lambda: 'test')
    assert Validation(None, []).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:32.348997
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    val = Validation.success(3)

    assert val.to_lazy() == Lazy(lambda: 3)

    val = Validation.fail([2, 3])

    assert val.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:36.264968
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success("value").to_lazy() == Lazy(lambda: "value")
    assert Validation.fail().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:13:39.552797
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    def f(x):
        return x + 1

    lazy_monad = Validation.success(1).to_lazy()
    assert lazy_monad.fmap(f)() == 2


# Generated at 2022-06-14 04:13:45.502868
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet import identity

    assert Validation.success(1).to_lazy() == Lazy(identity)
    assert Validation.success(1).to_try().get_result() == Try(1, True)
    assert Validation.success(1).to_maybe() == Maybe.just(1)
    assert Validation.success(1).to_box() == Box(1)
    assert Validation.success(1).to_either() == Right(1)


# Generated at 2022-06-14 04:13:48.813938
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.success(1)
    lazy_val = val.to_lazy()

    assert lazy_val == Lazy(lambda: 1)


# Generated at 2022-06-14 04:13:54.642174
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """It test method to_lazy of class Validation."""
    from pymonet.lazy import Lazy
    validation = Validation.success(10)
    lazy = validation.to_lazy()
    is_true(isinstance(lazy, Lazy))
    value = lazy.get_value()
    is_true(isinstance(value, Validation))
    is_true(value.is_success())
    is_equal(value.value, 10)
    is_equal(value.errors, [])

# Generated at 2022-06-14 04:14:02.182602
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    # GIVEN Validation
    validation = Validation.success(100)

    # WHEN to_lazy method is called and result is forced
    result = validation.to_lazy().force()

    # THEN result is equals to Validation value
    assert result == validation.value


# Generated at 2022-06-14 04:14:11.525633
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test that when Validation is successful then to_lazy returns Lazy with success value.
    """
    from pymonet.lazy import Lazy

    def calls_count():
        """Return number of function calls."""
        calls_count.counter = 0 if not hasattr(calls_count, 'counter') else calls_count.counter + 1
        return calls_count.counter

    value = calls_count()
    validation = Validation.success(value)
    assert validation.to_lazy() == Lazy(lambda: value), 'to_lazy should return Lazy with success value'
    assert calls_count() == 1, 'Lazy should be evaluated'

# Generated at 2022-06-14 04:14:15.465783
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:14:20.696621
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Failure, Success

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(1, []).to_lazy() != Lazy(lambda: 2)


# Generated at 2022-06-14 04:14:26.948390
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    def func():
        return 3

    validation = Validation.success(func)
    assert validation.to_lazy() == Lazy(func)

    assert validation.to_lazy().value() == 3
    assert validation.to_lazy().to_try() == Try.success(func)


# Generated at 2022-06-14 04:14:31.474497
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:14:32.732591
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(1, None).to_lazy().get() == 1
    assert Validation(None, { 'error': 'message' }).to_lazy().get() == None

# Generated at 2022-06-14 04:14:38.256242
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Success, Failure

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail(['first error']).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:14:43.902177
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:46.853204
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    validation_success = Validation.success(42)
    assert validation_success.to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 04:14:53.642811
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy = Lazy(lambda: 5)
    assert Validation.success(5).to_lazy() == lazy
    assert Validation.fail().to_lazy() == lazy



# Generated at 2022-06-14 04:14:57.499460
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_val import Validation
    from pymonet.lazy import Lazy

    _ = Validation(2, [])

    assert _.to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 04:15:02.673027
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)

    called = [0]
    assert Validation.success(42).to_lazy().eval() == 42
    assert called[0] == 1

# Generated at 2022-06-14 04:15:06.860325
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(1).to_lazy() == \
        Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == \
        Lazy(lambda: None)

# Generated at 2022-06-14 04:15:14.630528
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.function import Function
    from pymonet.lazy import Lazy
    from pymonet.functions import compose
    from pymonet.validation import Validation

    result = Function(Validation.success).apply(4).bind(Function(lambda v: Validation.success(v * 10))) \
        .bind(Function(lambda v: Validation.success(v / 2))).to_lazy()

    assert result == Lazy(Function(Function(Function(Validation.success(4)).map(lambda v: v * 10))
                                    .map(lambda v: v / 2)).apply)


# Generated at 2022-06-14 04:15:18.261984
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad import Monad

    v = Validation.success(1).to_lazy()
    assert Monad.is_instance(v)
    assert v.call() == 1


# Generated at 2022-06-14 04:15:20.644573
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def f():
        return 1 + 1
    validation = Validation.success(f())
    assert Lazy(f) == validation.to_lazy()


# Generated at 2022-06-14 04:15:27.949400
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy_1 = Validation.success(42).to_lazy()
    assert isinstance(lazy_1, Lazy)
    assert Try(42) == lazy_1.to_try()

    lazy_2 = Validation.fail(['bad request']).to_lazy()
    assert isinstance(lazy_2, Lazy)
    assert Try(None, is_success=False) == lazy_2.to_try()


# Generated at 2022-06-14 04:15:30.948516
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    from pymonet.lazy import Lazy

    assert Validation.success().to_lazy() == Lazy(lambda: None)
    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)

# Generated at 2022-06-14 04:15:37.749150
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.either import Right
    from pymonet.box import Box

    assert Try(1, is_success=True) == Validation.success(1).to_try()
    assert Try(1, is_success=False) == Validation.fail([1]).to_try()
    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([1]).to_lazy()
    assert Right(1) == Validation.success(1).to_either()
    assert Box(1) == Validation.success(1).to_box()
    assert Box(None) == Validation.fail([1]).to_box()
   

# Generated at 2022-06-14 04:15:47.076766
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy method of Validation class.
    """
    # GIVEN: Successful Validation with value
    validation = Validation.success("ok")
    # WHEN: Convertion to Lazy monad is performed
    lazy = validation.to_lazy()

    # THEN: Value of lazy is function that returns Validation value
    assert lazy.value() == "ok"


# Generated at 2022-06-14 04:15:48.715844
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    result = Validation.success('pymonet')
    assert result.to_lazy().force() == result.value

# Generated at 2022-06-14 04:15:51.697711
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    validation = Validation.success(5)
    assert validation.to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 04:15:57.549969
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    # test case for fail validation
    validation = Validation.fail([1, 2, 3])
    lazy = validation.to_lazy()
    assert lazy.get() == validation.value

    # test case for success validation
    validation = Validation.success(1)
    lazy = validation.to_lazy()
    assert lazy.get() == validation.value


# Generated at 2022-06-14 04:16:08.343624
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    # Create validation with positional argument
    v = Validation(42, [])

    # Transform Validation to Lazy
    l = v.to_lazy()
    assert isinstance(l, Lazy)

    # Get value from Lazy
    assert l.get() == 42

    # Create validation with keyword arguments
    v = Validation(value=42, errors=[])

    # Transform Validation to Lazy
    l = v.to_lazy()
    assert isinstance(l, Lazy)

    # Get value from Lazy
    assert l.get() == 42

    # Create validation for failure case
    v = Validation(errors=['test error'])

    # Transform Validation to Lazy
    l = v.to

# Generated at 2022-06-14 04:16:13.677446
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():          # pragma: no cover
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error_1']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:18.581584
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    result = Validation.success(3).to_lazy()
    assert isinstance(result, Lazy)
    assert result.eval() == 3

    result = Validation.fail([23, 45]).to_lazy()
    assert isinstance(result, Lazy)
    assert result.eval() is None


# Generated at 2022-06-14 04:16:24.852277
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # GIVEN
    val1 = Validation.success('value')
    val2 = Validation.fail('error')

    # WHEN
    lazy1 = val1.to_lazy()
    lazy2 = val2.to_lazy()

    # THEN
    assert lazy1.f() == 'value'
    assert lazy2.f() is None

# Generated at 2022-06-14 04:16:31.040225
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test for method to_lazy of class Validation."""
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def _f():
        return 1

    def _g():
        return 2

    assert Validation.success(1).to_lazy() == Lazy(_f) # Check function return function
    assert Validation.success(2).to_lazy() == Lazy(_g) # Check function return function


# Generated at 2022-06-14 04:16:33.374440
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().value() == 1


# Generated at 2022-06-14 04:16:45.987842
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    # Unit test for method to_lazy of class Validation
    validation = Validation(value=1, errors=[])
    assert validation.to_lazy() == Lazy(lambda: 1)

    validation = Validation(value=None, errors=[])
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:50.077436
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation with value '20' should be converted to Lazy with value '20'.
    """
    v = Validation.success(20)

    assert v.to_lazy().get() == 20



# Generated at 2022-06-14 04:16:53.013405
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    validation = Validation(1, [])
    assert validation.to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 04:16:56.282638
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation.to_lazy() unit test
    """
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 04:16:58.760520
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 04:17:01.762578
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy_success = Validation.success(1).to_lazy()
    assert lazy_success.value() == 1

    lazy_fail = Validation.fail().to_lazy()
    assert lazy_fail.value() is None


# Generated at 2022-06-14 04:17:03.861850
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    validation = Validation(123, [])
    assert validation.to_lazy() == Lazy(lambda: 123)


# Generated at 2022-06-14 04:17:14.096062
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.monad_try import Try
    from pymonet.monad_result import Result

    from pymonet.monad import do

    from pymonet.combinators import unit
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy

    v = Validation.success(10).to_lazy()

    with do(Lazy) as m:
        m.x = unit(10)
        m.y = v
        m.z = (m.x + m.y)
    assert m.z.force() == 20

    assert isinstance(v, Lazy)

    l = Lazy(lambda: 10)

    with do(Lazy) as m:
        m.x

# Generated at 2022-06-14 04:17:17.638822
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(3).to_lazy().get() == 3
    assert Validation.success(3).to_lazy().is_success() == True
    assert Validation.fail(["Some error occure"]).to_lazy().get() == None
    assert Validation.fail(["Some error occure"]).to_lazy().is_success() == False


# Generated at 2022-06-14 04:17:20.983877
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Validation.success(10).to_lazy()
    assert Lazy(lambda: None) == Validation.fail(['Error']).to_lazy()



# Generated at 2022-06-14 04:17:30.685431
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    v = Validation.success(5)
    assert v.to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 04:17:37.691470
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    assert Validation.success(5).to_lazy().value() == 5
    assert Validation.fail([1, 2, 3]).to_lazy().value() == None
    assert Validation.success(5).to_lazy().to_either() == Right(5)
    assert Validation.success(5).to_lazy().to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 04:17:43.590908
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    # Setup
    success_monad = Validation.success()
    fail_monad = Validation.fail([1])

    # Exercise
    success_lazy = success_monad.to_lazy()
    fail_lazy = fail_monad.to_lazy()

    # Verify
    assert isinstance(success_lazy, Lazy)
    assert isinstance(fail_lazy, Lazy)
    assert success_lazy.value() == None
    assert fail_lazy.value() == None


# Generated at 2022-06-14 04:17:50.530568
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    # Test for successful validation
    validation = Validation.success('value')
    assert isinstance(validation.to_lazy(), Lazy)
    assert validation.to_lazy().get() == 'value'
    assert isinstance(validation.to_try(), Try)
    assert validation.to_try().is_success()
    assert validation.to_try().get() == 'value'



# Generated at 2022-06-14 04:17:52.759910
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:17:55.597414
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test successful Validation"""
    validation = Validation.success('abc')

    assert validation.to_lazy().unsafe_run() == 'abc'
    assert validation.to_lazy().unsafe_run() == 'abc'


# Generated at 2022-06-14 04:17:59.047090
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Try.fail(1) == Lazy.unit(1).bind(Try.fail).to_try()
    assert Try.success(1) == Lazy.unit(1).bind(Try.success).to_try()


# Generated at 2022-06-14 04:18:02.081072
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().get() == 1

    assert Validation.fail([]).to_lazy().get() is None
    assert Validation.fail([1]).to_lazy().get() is None


# Generated at 2022-06-14 04:18:05.858621
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def foo(x):
        raise ValueError('Some error')

    lazy = Validation.fail(['Some error']).to_lazy()
    assert lazy.flat_map(foo).value() == 'Some error'



# Generated at 2022-06-14 04:18:08.944236
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(3).to_lazy().value() == 3
    assert Validation.fail(['error']).to_lazy().value() == None


# Generated at 2022-06-14 04:18:29.061158
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from operator import add
    from pymonet.monad_try import Try
    from pymonet.either import Left

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation(None, []).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation(Try(1), []).to_lazy() == Lazy(lambda: Try(1))

# Generated at 2022-06-14 04:18:34.082132
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Success, Failure

    success_value = 'Success!'
    validation = Validation.success(success_value)

    assert validation.to_lazy().take() == Success(success_value)

    failure_value = 'Failure!'
    validation = Validation.fail(failure_value)
    assert validation.to_lazy().take() == Failure(failure_value)



# Generated at 2022-06-14 04:18:40.893658
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    from pymonet.monad_try import Success, NoValue

    fn = lambda value: value ** 2
    value = 8

    validation = Validation.success(value)
    lazy = validation.to_lazy()
    assert lazy.value == fn(value)

    validation = Validation.fail()
    lazy = validation.to_lazy()
    assert lazy.value == NoValue


# Generated at 2022-06-14 04:18:45.770481
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    val = Validation.success(10)
    assert val.to_lazy().eval() == 10

    val = Validation.fail([])
    assert val.to_lazy().eval() == None

    val = Validation.fail(['error_1'])
    assert val.to_lazy().eval() == None

    val = Validation.fail(['error_1', 'error_2'])
    assert val.to_lazy().eval() == None


# Generated at 2022-06-14 04:18:50.501774
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from mock import Mock

    lazy = Mock(Lazy, spec=Lazy)
    value = Mock(spec=int)
    result = Validation.success(value).to_lazy()
    assert isinstance(result, Lazy)


# Generated at 2022-06-14 04:18:54.148060
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def test_value():
        return Validation.success(True)

    lazy = Validation.success(True).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.force() == test_value()


# Generated at 2022-06-14 04:18:57.472871
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    def func():
        return 1

    assert Validation.success(func).to_lazy() == Lazy(func)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:18:59.807180
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(5).to_lazy().force() == 5
    assert Validation.fail([1, 2]).to_lazy().force() is None

# Generated at 2022-06-14 04:19:05.613847
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    my_lazy = Lazy(lambda: 42)
    my_fail = Validation.fail([1, 2, 3])
    my_success = Validation.success(42)
    assert my_success.to_lazy() == my_lazy
    assert my_fail.to_lazy() == my_lazy



# Generated at 2022-06-14 04:19:09.478940
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.seq import Seq

    assert Seq(Validation.success(10).to_lazy().get()).first() == 10
    assert Seq(Validation.fail([1, 2, 3]).to_lazy().get()).first() == None

# Generated at 2022-06-14 04:19:30.480487
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().eval() == 1
    assert Validation.fail(1).to_lazy().eval() is None


# Generated at 2022-06-14 04:19:35.181783
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    val = Validation.success(1)
    res = val.to_lazy()
    assert res.evaluate() == 1
    val = Validation.fail()
    res = val.to_lazy()
    assert res.evaluate() is None


# Generated at 2022-06-14 04:19:41.608788
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(15).to_lazy() == Lazy(lambda: 15)
    assert Validation.success(15).to_lazy()().value == 15
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy()().value is None


# Generated at 2022-06-14 04:19:47.864468
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation_fail = Validation.fail(['some_error'])
    assert validation_fail.to_lazy() == Lazy(lambda: validation_fail.value)
    assert validation_fail.to_lazy().force() == Try(validation_fail.value, is_success=False)

    validation_success = Validation.success('something')
    assert validation_success.to_lazy() == Lazy(lambda: validation_success.value)
    assert validation_success.to_lazy().force() == Try(validation_success.value, is_success=True)


# Generated at 2022-06-14 04:19:49.983866
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(7).to_lazy() == Lazy(lambda: 7)

# Generated at 2022-06-14 04:19:57.859158
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:02.230319
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    result = Validation.fail(['error']).to_lazy()
    assert result == Lazy(lambda: None)

    result = Validation.success('somethig').to_lazy()
    assert result == Lazy(lambda: 'somethig')


# Generated at 2022-06-14 04:20:09.560179
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test case for testing transformation Validation to Lazy.

    """
    from pymonet.lazy import Lazy

    lazy = Validation.success(10).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 10
    assert lazy.is_computed()

    lazy = Validation.fail([]).to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() is None
    assert lazy.is_computed()


# Generated at 2022-06-14 04:20:14.253882
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.box import Box

    validation = Validation.success('value')
    assert validation.to_lazy() == Lazy(lambda: 'value')
    assert validation.to_lazy().value == 'value'

    validation = Validation.fail()
    assert validation.to_lazy() == Lazy(lambda: None)
    assert validation.to_lazy().value is None



# Generated at 2022-06-14 04:20:20.331274
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def add_three(x):
        return x + 3
    function = lambda: add_three(5)
    lazy = Validation.success(function).to_lazy()
    assert_that(lazy.value(), equal_to(8))
    assert_that(lazy.is_successful(), equal_to(True))
    assert_that(lazy.reason(), equal_to(None))


# Generated at 2022-06-14 04:21:01.269088
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(10).to_lazy().get() == 10
    assert Validation.fail().to_lazy().get() is None

# Generated at 2022-06-14 04:21:09.366375
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    # Lazy should return self
    assert Validation.success(0).to_lazy() == Lazy(lambda: 0)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success('abc').to_lazy() == Lazy(lambda: 'abc')

    # Method should return Lazy with function returning self value
    my_lazy = Validation.success('abc').to_lazy()
    assert my_lazy.value() == 'abc'
    assert my_lazy.value() == 'abc'
    assert my_lazy.value() == 'abc'


# Generated at 2022-06-14 04:21:14.741569
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)

    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:21:18.586619
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 1

    lazy = Lazy(func)

    assert Validation.success(2).to_lazy() == lazy
    assert Validation.fail().to_lazy() == lazy

# Generated at 2022-06-14 04:21:31.252186
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    lazy_val = Validation.success(lambda: 'test').to_lazy()
    assert isinstance(lazy_val, Lazy)
    assert lazy_val.computed is False
    assert lazy_val.value() == 'test'
    assert lazy_val.computed is True
    assert lazy_val.value() == 'test'

    lazy_val = Validation.fail(['er1', 'er2']).to_lazy()
    assert isinstance(lazy_val.value(), Try)
    assert lazy_val.value().is_failure()
    assert lazy_val.value().value() is None
