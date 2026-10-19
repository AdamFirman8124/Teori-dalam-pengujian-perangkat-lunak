

# Generated at 2022-06-14 04:11:32.458346
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    def func():
        return 10

    assert Validation.success(func).to_lazy() == Lazy(func)
    assert Validation.fail([1,2,3]).to_lazy() == Lazy(None)


# Generated at 2022-06-14 04:11:42.388625
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from functools import reduce

    def validation_adder(*args):
        accumulator = Validation.success(0)
        fold_fn = lambda a, b: a.ap(lambda _: b).map(lambda _: a.value + b.value)
        return reduce(fold_fn, args, accumulator)

    assert validation_adder(
        Validation.success(1),
        Validation.success(2),
        Validation.success(3)
    ).to_lazy().value() == 6

    assert validation_adder(
        Validation.success(1),
        Validation.success(2),
        Validation.fail(errors=[3]),
        Validation.success(4)
    ).to_lazy().value() == None

# Generated at 2022-06-14 04:11:51.220585
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.monad_try import Failure
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success("Hello").to_lazy() == Lazy(lambda: "Hello")
    assert Validation.fail("Failure").to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:11:55.210523
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It tests for method to_lazy.
    """
    from pymonet.lazy import Lazy

    lazy = Validation.success(10).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.eval() == 10


# Generated at 2022-06-14 04:11:59.902385
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:01.072294
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Success(10).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 04:12:04.827969
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def test_success():
        return Validation.success(10)

    def test_fail():
        return Validation.fail([])

    assert test_success().to_lazy() == Lazy(lambda: 10)
    assert test_fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:11.997571
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.exceptions import PymonetException

    def error_func():
        raise PymonetException("exception raised")

    def success_func():
        return 1

    lazy_fail = Validation.fail(['error_lazy']).to_lazy()
    lazy_success = Validation.success(1).to_lazy()

    assert lazy_fail.value() == None
    assert lazy_success.value() == 1

    lazy_success.value = error_func
    lazy_fail.value = success_func

    assert lazy_fail.value() == 1
    assert lazy_success.value() == None

# Generated at 2022-06-14 04:12:23.442191
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.either import Left, Right
    from pymonet.validation import Validation


# Generated at 2022-06-14 04:12:27.951564
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    value = Validation.success(5)
    lazy_value = value.to_lazy()
    assert value == Lazy(lambda: 5).eval()

# Generated at 2022-06-14 04:12:36.782535
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def start_with(prefix):
        def func(string):
            return prefix + string
        return func

    valid_string = Validation.success('string value')
    assert isinstance(valid_string.to_lazy(), Lazy)
    assert valid_string.to_lazy().__value__ == 'string value'

    invalid_string = Validation.fail(['value is None'])
    assert isinstance(invalid_string.to_lazy(), Lazy)
    assert invalid_string.to_lazy().__value__ == None

    assert isinstance(valid_string.to_lazy().map(start_with('prefix ')), Lazy)
    assert valid_string.to_lazy().map(start_with('prefix ')).__value__ == 'prefix string value'

# Generated at 2022-06-14 04:12:43.696640
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def is_lazy_instance_of_lazy(lazy):
        return isinstance(lazy, Lazy)

    assert is_lazy_instance_of_lazy(Validation.success(10).to_lazy())
    assert is_lazy_instance_of_lazy(Validation.fail([1, 2, 3]).to_lazy())


# Generated at 2022-06-14 04:12:49.384005
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy of class Validation
    """
    def test_function():
        """
        Helper test function for Validation test_to_lazy method.
        """
        return Validation.success('success')

    assert test_function().to_lazy().get() == 'success'


# Generated at 2022-06-14 04:12:55.333078
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    from pymonet.monad_maybe import Maybe

    def run_5_times(value):
        from pymonet.monad_try import Try
        return Try(lambda: value * 5)

    validation = Validation.success(4).to_lazy()

    assert validation == Lazy(lambda: 4)

    with pytest.raises(ZeroDivisionError):
        validation.bind(run_5_times).value()

    # Test for map

    assert validation.map(lambda x: x * 5).value() == 20

    # Test for bind

    assert validation.bind(run_5_times).value() == 20

    # Test for ap

    assert validation.ap(Maybe.just(run_5_times)).value() == 20

# Generated at 2022-06-14 04:13:04.389664
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from functools import reduce

    assert Lazy(lambda: 2) == Validation.success(2).to_lazy()
    assert Lazy(lambda: reduce(lambda acc, el: acc + el, [1, 2, 3, 4, 5])) == reduce(lambda acc, el: acc + el, [1, 2, 3, 4, 5]).to_lazy()
    assert Lazy(lambda: 'test') == 'test'.to_lazy()
# endregion
# region Validators

# Generated at 2022-06-14 04:13:07.880376
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad import unit_test_monad
    from pymonet.lazy import Lazy
    unit_test_monad(Validation, success_value='value', failure_value=['error'], to_lazy=Lazy)


# Generated at 2022-06-14 04:13:12.871779
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 50) == Validation.success(50).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()
    assert Lazy(lambda: 50) == Validation.success(50).to_try().to_lazy()


# Generated at 2022-06-14 04:13:19.417048
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.functor import Functor

    lazy = Validation.success('value').to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: 'value')
    assert lazy.get() == Functor.identity('value')

    lazy = Validation.fail(['error']).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: None)
    assert lazy.get().to_either().is_left()

    lazy = Validation.Fail(['error']).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy == Lazy(lambda: None)

# Generated at 2022-06-14 04:13:24.778003
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # When method to_lazy is called on successful Validation
    lazy = Validation.success(123).to_lazy()

    # Then result is Lazy monad with function returning value stored in Validation
    assert isinstance(lazy, Lazy)
    assert lazy() == 123



# Generated at 2022-06-14 04:13:30.674010
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: 1) == Validation.fail([]).to_lazy()
    assert Lazy(lambda: 1) == Validation.fail(['Error']).to_lazy()


# Generated at 2022-06-14 04:13:36.355625
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().get() == 1


# Generated at 2022-06-14 04:13:38.884559
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    v = Validation.success(10)
    t = v.to_lazy()

    assert t.value() == 10


# Generated at 2022-06-14 04:13:41.568834
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(5).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.func() == 5


# Generated at 2022-06-14 04:13:46.997698
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # If Validation is success
    success_validation = Validation(5, [])

    assert success_validation.to_lazy().get() == 5

    # If Validation is fail
    fail_validation = Validation(None, [1, 2, 3])

    assert fail_validation.to_lazy().get() == None



# Generated at 2022-06-14 04:13:52.683455
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.monad_lazy import Lazy
    from pymonet.box import Box

    assertion = Validation.fail(['fail 1', 'fail 2'])
    assert assertion.to_lazy() == Lazy(lambda: None)

    assertion = Validation.success(Box(Try(1)))
    assert assertion.to_lazy() == Lazy(lambda: Box(Try(1)))

# Generated at 2022-06-14 04:13:57.572603
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    val = Validation(1, [2])
    lazy = val.to_lazy()

    assert isinstance(lazy, Lazy)
    assert isinstance(lazy.run(), Try)



# Generated at 2022-06-14 04:14:07.741106
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It takes as a parameter function returning another Validation.
    Function is called with Validation value and returns new Validation with previous value
    and concated new and old errors.

    :param monad: monad contains function
    :type monad: Function(A) -> Validation[Any, List[E]]
    :returns: new validation with stored errors
    :rtype: Validation[A, List[E]]
    """
    assert Validation(10, []).to_lazy() == Lazy(lambda: 10)
    assert Validation(None, [10]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:10.229680
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: Validation.success(2))

    assert Validation.success(2) == lazy.force()

# Generated at 2022-06-14 04:14:16.556971
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    result = Validation.success(10).to_lazy()
    assert result == Lazy(lambda: 10)
    assert result.get() == 10
    result = Validation.fail(errors=[1, 2, 3]).to_lazy()
    assert result == Lazy(lambda: None)
    assert result.get() is None


# Generated at 2022-06-14 04:14:22.597597
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy method of class Validation.
    """
    from pymonet.monad_try import Try

    assert Try(1) == Validation.success(1).to_lazy().to_try()
    assert Try(None, is_success=False) == Validation.fail([]).to_lazy().to_try()

# Generated at 2022-06-14 04:14:35.769157
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.success(10)
    assert val.to_lazy() == Lazy(lambda: 10)

    val = Validation.fail([InvalidArgumentError('failed')])
    assert val.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:41.775460
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Failure, Success

    assert Validation.success(value=1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(errors=[
        'something wrong'
    ]).to_lazy() == Lazy(lambda: None)

# Unit testing for method ap of class Validation

# Generated at 2022-06-14 04:14:44.769927
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:48.090987
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test transform validation to Lazy.

    :returns: True for success, else raise Assertion error
    :rtype: Boolean
    """
    validation = Validation.success(True)
    lazy_monad = validation.to_lazy()
    return lazy_monad() is True


# Generated at 2022-06-14 04:14:53.838534
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    v = Validation.success(10).to_lazy()
    assert v == Lazy(lambda: 10)

    v = Validation.fail(['error']).to_lazy()
    assert v == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:57.300897
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(True).to_lazy() == Lazy(lambda: True)
    assert Validation.fail([True, True]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:08.529719
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    lazy_a = Lazy.unit(Validation).to_lazy()
    assert(lazy_a.eval() == Validation.success())

    lazy_a = Lazy.unit(Validation).ap(Lazy.unit(lambda x: Validation.success(x + 10))).to_lazy()
    assert(lazy_a.eval() == Validation.success(10))

    lazy_b = Lazy.unit(Validation).ap(Lazy.unit(lambda x: Validation.fail(['error']))).to_lazy()
    assert(lazy_b.eval() == Validation.fail(['error']))

if __name__ == '__main__':  # pragma: no cover
    test_Val

# Generated at 2022-06-14 04:15:11.851784
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    # When: Call to_lazy method from Validation
    # Then: Lazy instance is returned
    assert Validation.success(3).to_lazy().force() == 3
    assert Validation.fail().to_lazy().force() is None

# Generated at 2022-06-14 04:15:18.218434
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation


    lazy = Validation.success().to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy() == None

    lazy = Validation.success('test').to_lazy()

    assert lazy() == 'test'

# Generated at 2022-06-14 04:15:23.036613
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def func(value):
        return value * 2

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.success(5).to_lazy().map(func) == Lazy(lambda: 10)
    assert Validation.success(5).to_lazy().map(func).get() == 10


# Generated at 2022-06-14 04:15:40.396826
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.success(5).to_lazy()
    assert lazy.get_value() == 5

    lazy = Validation.success(6).to_lazy()
    assert lazy.get_value() == 6

    lazy = Validation.fail().to_lazy()
    assert lazy.get_value() is None



# Generated at 2022-06-14 04:15:43.190142
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 04:15:49.189794
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # test for success validation
    validation_success = Validation.success(10)
    assert validation_success.to_lazy() == Lazy(lambda: 10), 'Error with successful Validation'

    # test for failed validation
    validation_failed = Validation.fail([1, 2, 3])
    assert validation_failed.to_lazy() == Lazy(lambda: None), 'Error with failed Validation'


# Generated at 2022-06-14 04:15:53.815035
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Failure, Success

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:15:56.110077
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    success = Validation.success(10)
    assert success.to_lazy() == Lazy(lambda: 10)

    fail = Validation.fail([1, 2, 3])
    assert fail.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:15:59.298594
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    f = lambda: '42'
    l = Lazy(f).to_validation().to_lazy()
    assert l().value == f().value

# Generated at 2022-06-14 04:16:06.884292
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left

    lazy = Validation.success(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 1
    assert Validation.fail().to_lazy().get() is None

    assert Validation.fail([1, 2]).to_lazy().to_either() == Left([1, 2])
    assert Validation.success(1).to_lazy().to_either() == Left([])


# Generated at 2022-06-14 04:16:09.979528
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    def test():
        return Validation.success(1)

    assert Validation.success(1).to_lazy() == Lazy(test)
    assert Validation.fail(['1']).to_lazy() == Lazy(test)


# Generated at 2022-06-14 04:16:15.503619
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:20.965278
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.success(10).to_lazy().flat_map(lambda v: Lazy(lambda: v + 10)) == Lazy(lambda: 20)
    assert Validation.success(10).to_lazy().map(lambda v: v + 10) == Lazy(lambda: 20)
    assert Validation.success(10).to_lazy().map(lambda v: v + 10).run() == 20


# Generated at 2022-06-14 04:16:58.076351
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Success
    from pymonet.either import Right

    # Case 1: Validation.Success(Success(Right("Success")))
    validation = Validation.success(Success(Right("Success")))
    lazy = validation.to_lazy()
    assert (lazy == Lazy(lambda: Success(Right("Success"))))

    # Case 2: Validation.Fail([Exception("Error 1", Exception("Error 2"))])
    validation = Validation.fail([Exception("Error 1"), Exception("Error 2")])
    lazy = validation.to_lazy()
    assert (lazy == Lazy(lambda: None))


# Generated at 2022-06-14 04:17:02.480009
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1), 'Wrong lazy result'

    # Result should return 1 when is called
    assert Validation.success(1).to_lazy().get() == 1, 'Wrong lazy result'



# Generated at 2022-06-14 04:17:07.345489
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test transformation Validation to Lazy monad.

    :return: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Lazy(lambda: 'x') == Validation.success('x').to_lazy()


# Generated at 2022-06-14 04:17:11.415346
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def func(a):
        return a + 2

    lazy = Validation.success(100).to_lazy()
    assert lazy.map(func) == 102

    lazy = Validation.fail([100, 200]).to_lazy()
    assert lazy.map(func) is None



# Generated at 2022-06-14 04:17:15.573066
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functions import identity

    validation = Validation.success(Foo(42))

    assert validation.to_lazy() == Lazy(lambda: Foo(42))
    assert validation.to_lazy().fmap(identity) == Lazy(lambda: Foo(42))


# Generated at 2022-06-14 04:17:19.494136
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def create_lazy():
        return Lazy(lambda: Validation.success(1))

    assert create_lazy() == Validation.success(1).to_lazy()



# Generated at 2022-06-14 04:17:22.110363
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:17:26.242331
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def function():
        return 5

    assert Validation.success(5).to_lazy() == Lazy(function)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:30.555400
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Success, Failure
    """
    Test function tries to transform Validation to Lazy.
    """
    assert Lazy(lambda: 10) == Validation.success(10).to_lazy()
    assert Lazy(lambda: 10) == Validation.fail(["error"]).to_lazy()



# Generated at 2022-06-14 04:17:40.439639
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['Error 1']).to_lazy() == Lazy(lambda: None)

    assert Validation.success(1).to_lazy().to_box() == Box(1)
    assert Validation.fail(['Error 1']).to_lazy().to_try() == Try(None, is_success=False)

    assert Validation.success(1).to_lazy().to_maybe() == Maybe.just(1)
    assert Validation.fail(['Error 1']).to_lazy().to_maybe() == Maybe.nothing()


# Generated at 2022-06-14 04:18:50.240417
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    value = 1
    validation_with_errors = Validation.fail([value])
    validation_without_errors = Validation.success(value)

    assert Validation.success(value).to_try() == Try(value, True)
    assert Validation.fail([]).to_try() == Try(None, False)



# Generated at 2022-06-14 04:18:54.268015
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'a') == Validation.success('a').to_lazy()
    assert Lazy(lambda: None) == Validation.fail().to_lazy()

    # Unit test for method to_try of class Validation

# Generated at 2022-06-14 04:18:58.350200
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # GIVEN
    val = Validation.success('result')
    lazy_val = Lazy(lambda: 'result')

    # THEN
    assert val.to_lazy() == lazy_val, 'Validation value is stored in Lazy monad'

# Generated at 2022-06-14 04:19:03.454780
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    val = Validation(1, [])
    assert val.to_lazy() == Lazy(lambda: 1)
    val = Validation(None, [])
    assert val.to_lazy() == Lazy(lambda: None)
    val = Validation(1, [])
    assert val.to_try() == Try(1)
    val = Validation(None, [])
    assert val.to_try() == Try(None, False)

if __name__ == '__main__':  # pragma: no cover
    test_Validation_to_lazy()

# Generated at 2022-06-14 04:19:06.063786
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Try(1) == Try(Lazy(lambda: 1).to_try())

# Generated at 2022-06-14 04:19:09.514581
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:21.456372
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    import pymonet.lazy
    from pymonet.maybe import Maybe

    # When Validation contains value
    val = Validation.success('Python')
    lazy_val = val.to_lazy()

    assert isinstance(lazy_val, pymonet.lazy.Lazy)
    result = lazy_val.map(lambda x: x.upper())

    assert isinstance(result, Maybe)
    assert result == Maybe.just('PYTHON')

    # When Validation is fail
    val = Validation.fail()
    lazy_val = val.to_lazy()

    assert isinstance(lazy_val, pymonet.lazy.Lazy)
    result = lazy_val.map(lambda x: x.upper())

    assert isinstance(result, Maybe)
    assert result == Maybe.nothing()

# Generated at 2022-06-14 04:19:25.457834
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.evaluate_now() == validation.value

# Generated at 2022-06-14 04:19:32.207563
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    _ = """
    It transforms Validation to Lazy
    """
    # when
    validation_success = Validation.success('value')

    # then
    assert validation_success.to_lazy().resolve() == 'value'

    # when
    validation_fail = Validation.fail()

    # then
    assert validation_fail.to_lazy().resolve() is None

test_Validation_to_lazy()


# Generated at 2022-06-14 04:19:43.781917
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.identity import Identity
    from pymonet.may import Just, Nothing

    result = Validation.success(100).to_lazy()
    assert isinstance(result, Lazy)
    assert result.perform() == 100

    result = Validation.fail(["error1", "error2"]).to_lazy()
    assert isinstance(result, Lazy)
    assert result.perform() == None

    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.fail(["error1", "error2"]).to_lazy() == Lazy