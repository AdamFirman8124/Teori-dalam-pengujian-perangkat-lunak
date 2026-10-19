

# Generated at 2022-06-14 04:11:39.367821
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    lazy = Validation.fail([1, 2, 3]).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.invoke() == None

    lazy = Validation.success(42).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.invoke() == 42

    lazy = Validation.fail([1, 2, 3]).map(lambda x: x * 2).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.invoke() == None

    lazy = Validation.success(42).map(lambda x: x * 2).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.invoke

# Generated at 2022-06-14 04:11:40.454218
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(5)
    lazy = validation.to_lazy()
    assert lazy.get() == 5


# Generated at 2022-06-14 04:11:42.917373
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(11).to_lazy() == Lazy(lambda: 11)


# Generated at 2022-06-14 04:11:49.811813
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy

    # test for lazy monad
    lazy_result = Lazy(lambda: 'value')

    assert lazy_result.to_lazy().compose(lambda param: param)() == 'value'
    assert lazy_result.to_lazy().map(lambda param: param)() == 'value'

    assert lazy_result.to_lazy().compose(lambda param: Maybe.just(param)).compose(lambda maybe: maybe.value)() == 'value'
    assert lazy_result.to_lazy().map(lambda param: Maybe.just(param)).compose(lambda maybe: maybe.value)() == 'value'

    # test for maybe monad


# Generated at 2022-06-14 04:11:55.964679
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    v1 = Validation.success(2)
    v2 = v1.to_lazy()
    assert v1 == v2.run()
    assert v1 == Lazy(lambda: v2.run()).run()
    assert Try(v2.run()).map(lambda x: x*2).or_else(0) == 4

# Generated at 2022-06-14 04:11:59.263707
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assertion = Validation.success([1]).to_lazy()
    assert isinstance(assertion, Lazy)
    assert assertion.force() == [1]


# Generated at 2022-06-14 04:12:04.376068
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet import maybe

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail(errors=('some error',)).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:09.384959
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([10]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:16.516096
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(1, [1]).to_lazy() == Lazy(lambda: 1)
    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(None, [1]).to_lazy() == Lazy(lambda: None)
    assert Validation(None, []).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:12:23.449364
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    validation = Validation(1, [])
    assert validation.to_lazy() == Lazy(lambda: 1)
    validation = Validation(None, [{'error': 'error'}])
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:30.916897
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy1 = Validation.success(1).to_lazy()
    lazy2 = Validation.success(1).to_lazy()

    assert(lazy1 != lazy2)
    assert(lazy1.is_equals(lazy2))


# Generated at 2022-06-14 04:12:39.063026
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_validation import Validation

    test_value = 'test_value'
    test_errors = ['test_error']

    validation = Validation(test_value, test_errors)
    lazy = validation.to_lazy()
    assert lazy == Lazy(lambda: validation.value)
    assert lazy.get() == test_value


# Generated at 2022-06-14 04:12:46.264057
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad import unit

    success_validation = Validation.success('value')
    success_lazy = success_validation.to_lazy()

    fail_validation = Validation.fail(['error'])
    fail_lazy = fail_validation.to_lazy()

    assert success_lazy == unit('value')
    assert success_lazy.to_try() == Try('value')
    assert fail_lazy.to_try() == Try(None, False)


# Generated at 2022-06-14 04:12:51.152256
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    lazy_1 = Validation.success(10).to_lazy()
    lazy_2 = Validation.fail([1, 2]).to_lazy()

    assert lazy_1 == Lazy(lambda: 10)
    assert lazy_2 == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:57.264074
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success('a').to_lazy() == Lazy(lambda: 'a')
    assert Validation.fail(['b']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:05.048390
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """Unit test for method to_lazy of class Validation"""

    from pymonet.lazy import Lazy

    success_validation = Validation.success('test')
    assert success_validation.to_lazy() == Lazy(lambda: 'test')
    fail_validation = Validation.fail(['error'])
    assert fail_validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:08.373258
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test transformation Validation to Lazy
    """
    from pymonet.lazy import Lazy

    validation = Validation.success(value=123)
    lazy = validation.to_lazy()
    assert lazy == Lazy(123)


# Generated at 2022-06-14 04:13:13.606423
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.either import Right
    from pymonet.monad_try import Try

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert (Try(1, is_success=True).to_lazy() == Lazy(lambda: 1))
    assert (Try(2, is_success=False).to_lazy() == Lazy(lambda: 2))

# Generated at 2022-06-14 04:13:17.469185
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    lazy = Validation.success(Box(1)).to_lazy()

    assert lazy.is_instance_of(Lazy)
    assert lazy.force() == Box(1)


# Generated at 2022-06-14 04:13:20.995607
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def func():
        return 'value'
    v = Validation.success('value')
    assert v.to_lazy() == Lazy(func)


# Generated at 2022-06-14 04:13:28.158052
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    # given
    lazy = Validation(5, []).to_lazy()

    # then
    assert lazy.value() == 5


# Generated at 2022-06-14 04:13:33.250665
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    _validation = Validation.success(2)
    assert _validation.to_lazy() == Lazy(lambda: 2)

    _validation = Validation.fail([Try.TypeError, Try.ValueError])
    assert _validation.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:13:39.789413
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    def func(x):
        return x + 2

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy().map(func) == Lazy(lambda: 3)

# Generated at 2022-06-14 04:13:43.151920
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success([1, 2, 3]).to_lazy() == Lazy([1, 2, 3])
    assert Validation.fail('error').to_lazy() == Lazy(None)


# Generated at 2022-06-14 04:13:47.152030
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:51.947739
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given
    success = Validation.success("test")
    failure = Validation.fail(["test"])

    # When
    result_success = success.to_lazy()
    result_failure = failure.to_lazy()

    # Then
    assert result_success.value() == "test"
    assert result_failure.value() == None


# Generated at 2022-06-14 04:13:55.226954
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.fail([ValueError, TypeError]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:59.364546
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Success, Failure

    # when
    lazy = Validation.success(1).to_lazy()
    try1 = lazy.eval()
    try2 = lazy.eval()

    # then
    assert isinstance(try1, Success)
    assert isinstance(try2, Success)
    assert try1.value == 1
    assert try2.value == 1


# Generated at 2022-06-14 04:14:03.962545
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    helper = Validation.success(5)
    assert helper.to_lazy() == Lazy(lambda: 5)

    helper = Validation.fail([1, 2, 3])
    assert helper.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:14:07.289120
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.funcs import add

    assert Validation.success(30).to_lazy().bind(add, 10).force() == 40

# Generated at 2022-06-14 04:14:15.528808
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.fail(['error 1']).to_lazy().get() is None
    assert Validation.success(1).to_lazy().get() == 1


# Generated at 2022-06-14 04:14:23.847935
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy() != Lazy(lambda: 2)

    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() != Lazy(lambda: 1)



# Generated at 2022-06-14 04:14:27.006617
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:14:38.919040
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""
    def test_result(expected, actual):
        assert isinstance(actual, Lazy)

        if expected is None:
            assert isinstance(actual.value, type(None))
        else:
            assert expected == actual.value

    from pymonet.lazy import Lazy

    # None as Validation value, successful Validation
    test_result(None, Validation.success(None).to_lazy())

    # None as Validation value, failed Validation
    test_result(None, Validation.fail([]).to_lazy())

    # 1 as Validation value, successful Validation
    test_result(1, Validation.success(1).to_lazy())

    # 1 as Validation value, failed Validation

# Generated at 2022-06-14 04:14:46.565708
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    # Test when Validation is successful
    def get_validation():
        """Return successful Validation."""
        return Validation.success(1)

    lazy = get_validation().to_lazy()
    assert lazy.value() == 1

    # Test when Validation is failed
    def get_failed_validation():
        """Return failed Validation."""
        return Validation.fail(['failed'])

    lazy = get_failed_validation().to_lazy()
    assert lazy.value() == None

# Generated at 2022-06-14 04:14:57.969430
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """

    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation(123, []).to_lazy() == Lazy(lambda: 123)
    assert Validation('Hello', []).to_lazy() == Lazy(lambda: 'Hello')
    assert Validation(None, []).to_lazy() == Lazy(lambda: None)
    assert Validation(False, []).to_lazy() == Lazy(lambda: False)
    assert Validation(True, []).to_lazy() == Lazy(lambda: True)
    assert Validation(9.99, []).to_lazy() == Lazy(lambda: 9.99)



# Generated at 2022-06-14 04:15:07.726883
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy.unit(lambda: 1).flat_map(lambda x: Lazy.unit(x)) == Lazy.unit(lambda: 2)
    assert Lazy.unit(lambda: 2).flat_map(lambda x: Lazy.unit(x)) == Lazy.unit(lambda: 4)
    assert Lazy.unit(lambda: 3).flat_map(lambda x: Lazy.unit(x)) == Lazy.unit(lambda: 6)
    assert Lazy.unit(lambda: 4).flat_map(lambda x: Lazy.unit(x)) == Lazy.unit(lambda: 8)


# Generated at 2022-06-14 04:15:09.513873
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('success').to_lazy() == Lazy(lambda: 'success')


# Generated at 2022-06-14 04:15:13.038866
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    try_ = Try.unit(None, is_success=False)
    assert try_.to_lazy().call() == Validation.fail().value

    try_ = Try.unit("A")
    assert try_.to_lazy().call() == Validation.success("A").value


# Generated at 2022-06-14 04:15:23.663736
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: nocover
    from pymonet.lazy import Lazy

    def is_even(x):
        return x % 2 == 0

    def get_number(x):
        return x * 2

    validation = Validation.fail([Exception('Boom')])
    print(validation.to_lazy().get_or_else(0))
    validation = Validation.success(4)
    print(validation.to_lazy().get_or_else(0))

    validation = Validation.fail([Exception('Boom')])
    print(validation.to_lazy().map(is_even))

    validation = Validation.success(4)
    print(validation.to_lazy().map(is_even))

    validation = Validation.fail([Exception('Boom')])

# Generated at 2022-06-14 04:15:32.846246
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    # Prerequisites
    validation = Validation(1, [])

    # Execute
    lazy = validation.to_lazy()

    # Assertions
    assert lambda: Try(1, is_success=True) == lazy.value, 'Validation.to_lazy() should return Lazy with function returning Try(1, True)'

# Generated at 2022-06-14 04:15:42.776207
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Success, Failure

    success = Validation.success('ok')
    try_success = Success('ok')
    lazy_success = success.to_lazy()
    lazy_success_lambda = lazy_success.get()
    assert success == lazy_success_lambda()
    assert success == lazy_success()
    assert try_success == lazy_success.to_try()

    fail = Validation.fail(['this is error'])
    try_fail = Failure('this is error')
    lazy_fail = fail.to_lazy()
    assert fail == lazy_fail()
    assert try_fail == lazy_fail.to_try()


# Generated at 2022-06-14 04:15:48.813967
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    val = Validation.success(Try.success(lambda a: a + 1))
    lazy = val.to_lazy()

    assert lazy == Lazy(lambda: Try.success(lambda a: a + 1))

    val = Validation.fail([])
    lazy = val.to_lazy()

    assert lazy == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:54.865501
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy method of Validation class

    """
    from pymonet.lazy import Lazy

    def get_val():
        return 'test'

    assert Validation.success('test').to_lazy() == Lazy(get_val)
    assert Validation.fail(['test']).to_lazy() == Lazy(get_val)


# Generated at 2022-06-14 04:15:59.174813
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Lazy(lambda : 10) == Validation(10, []).to_lazy()
    assert Lazy(lambda : None) == Validation(None, [1, 2]).to_lazy()



# Generated at 2022-06-14 04:16:03.397949
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    test_Validation_to_lazy: Tests that Validation.success.to_lazy() returns `Lazy(lambda: 42)`
    """
    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)

# Generated at 2022-06-14 04:16:06.302352
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return Validation.success(3).value

    assert Validation.success(3).to_lazy() == Lazy.pure(func)

# Generated at 2022-06-14 04:16:08.618774
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def _foo():
        return 1

    lazy = Validation.success(_foo).to_lazy()
    assert lazy.force() == 1


# Generated at 2022-06-14 04:16:17.789962
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success('a').to_lazy() == Lazy(lambda: 'a')


if __name__ == '__main__':  # pragma: no cover
    test_Validation_to_lazy()

# Generated at 2022-06-14 04:16:22.895213
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 04:16:33.374773
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    value = 10
    assert Lazy(lambda: value) == Validation.success(value).to_lazy()
    assert Lazy(lambda: value) == Validation.success(value).to_lazy()


# Generated at 2022-06-14 04:16:36.908608
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success("abc").to_lazy() == Lazy("abc")
    assert Validation.fail(["Error 1"]).to_lazy() == Lazy(None)


# Generated at 2022-06-14 04:16:43.870529
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test for to_lazy method of Validation class."""
    from pymonet.lazy import Lazy
    test_value = 1
    validation = Validation(test_value, [])
    assert validation.to_lazy() == Lazy(lambda: test_value)

# Generated at 2022-06-14 04:16:47.911631
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    v = Validation.success(42)
    assert v.to_lazy() == Lazy(lambda: 42)
    v = Validation.success(42)
    assert Lazy(lambda: 42) == v.to_lazy()


# Generated at 2022-06-14 04:16:55.401035
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:16:58.601565
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    val = Validation.success(1)
    assert val.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:17:03.534587
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    def fn():
        return 5

    def is_equal(laz1, laz2):
        return laz1.value() == laz2.value()

    assert is_equal(Validation.success(5).to_lazy(), Lazy(fn))
    assert not is_equal(Validation.fail([]).to_lazy(), Lazy(fn))



# Generated at 2022-06-14 04:17:06.472081
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 04:17:10.572853
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    validate = Validation.success(10)
    assert isinstance(validate.to_lazy(), Lazy)
    validate = Validation.fail(['error'])
    assert isinstance(validate.to_lazy(), Lazy)


# Generated at 2022-06-14 04:17:14.785698
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.validation import Validation

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:17:29.746216
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def first_name_provider():
        return 'Ewan'
    def second_name_provider():
        return 'Thompson'

    validation = Validation.success(first_name_provider)
    assert (validation.to_lazy() == Lazy(first_name_provider))
    validation = Validation.success(second_name_provider)
    assert (validation.to_lazy() == Lazy(second_name_provider))


# Generated at 2022-06-14 04:17:33.620047
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:17:40.588856
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Failure
    from pymonet.monad_try import Success

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['a', 'b']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(Failure(1)).to_lazy().run() == Failure(1)
    assert Validation.success(Success(1)).to_lazy().run() == Success(1)


# Generated at 2022-06-14 04:17:46.708908
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.monad import do
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def test_function(value):
        """test function"""
        return Lazy(lambda: value)

    @do(Lazy)
    def action():
        """test action"""
        validation = yield Validation.success(123)
        result = yield test_function(validation)
        return result

    assert action().run() == 123

# Generated at 2022-06-14 04:17:53.392488
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    success_validation = Validation.success(10)
    failure_validation = Validation.fail([1, 2, 3])

    assert Validation.success(10).to_lazy().value() == success_validation.value
    assert Validation.fail([1, 2, 3]).to_lazy().value() == failure_validation.value


# Generated at 2022-06-14 04:17:58.858480
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # given
    from pymonet.maybe import Maybe
    from functools import reduce

    # when
    validation = Validation.fail(['A', 'B', 'C'])
    validation2 = Validation.success([1, 2, 3, 4, 5])

    # then
    assert validation.to_lazy() == Lazy(lambda: None)
    assert validation2.to_lazy().map(lambda value: reduce(lambda a, b: a + b, value)) == Lazy(lambda: 15)


# Generated at 2022-06-14 04:18:01.377793
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(3, []).to_lazy() != Lazy(lambda: 4)
    assert Validation(3, []).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 04:18:06.961334
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test checks that value stored in Lazy is the same one stored in Validation.
    """
    value = 'value'
    validation = Validation(value, [])
    lazy = validation.to_lazy()

    assert validation.value == lazy()

if __name__ == '__main__':  # pragma: no cover
    test_Validation_to_lazy()

# Generated at 2022-06-14 04:18:10.961821
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    from pymonet.lazy import Lazy

    lazy_func = lambda: 3

    validation = Validation.success(lazy_func)

    assert validation.to_lazy() == Lazy(lambda: lazy_func)


# Generated at 2022-06-14 04:18:15.692692
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """
    It tests if Lazy monad returned from Validation holds same value as Validation.
    If not it will raise AssertionError.
    """
    from pymonet.lazy import Lazy

    for test_value in [1, 100, 10000, 1000000]:
        assert test_value == Lazy(lambda: test_value).force()

# Generated at 2022-06-14 04:18:29.151861
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.success(4)
    assert val.to_lazy() == Lazy(lambda: 4)

    val = Validation.fail([1, 2, 3])
    assert val.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:32.482063
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    def get_value():
        return 'success'
    assert Validation.success(get_value()).to_lazy() == Lazy(get_value)


# Generated at 2022-06-14 04:18:36.848334
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:18:39.881938
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    value = 1
    validation = Validation.success(value)
    assert validation.to_lazy() == Lazy(lambda: value)



# Generated at 2022-06-14 04:18:44.325742
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # Setup:
    value = 1
    errors = ['not valid']

    # Exercise:
    validation = Validation(value, errors)
    lazy = validation.to_lazy()

    # Verify:
    assert isinstance(lazy, Lazy)
    assert lazy() == value # pylint: disable=W0106



# Generated at 2022-06-14 04:18:47.844391
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_func():
        return 2

    lazy = Validation.success(test_func).to_lazy()
    assert lazy.get_value() == 2



# Generated at 2022-06-14 04:18:52.341232
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test for Validation to_lazy method.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 42) == Validation.success(42).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()

# Generated at 2022-06-14 04:18:56.524497
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    # When
    v = Validation(Maybe.just(5), [])
    lazy = v.to_lazy()

    # Then
    assert isinstance(lazy, Lazy)
    assert lazy() == 5

# Generated at 2022-06-14 04:19:00.294306
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Success, Failure

    assert Success.success(2).to_lazy() == Lazy(lambda: 2)
    assert Failure('error').to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:03.796093
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def lazy_return_value():
        return 10

    test_value = Validation.success(lazy_return_value)

    assert test_value.to_lazy().value() == 10


# Generated at 2022-06-14 04:19:18.981966
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Tests method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy
    value = 'value'
    validation = Validation(value, None)
    lazy = validation.to_lazy()
    assert lazy == Lazy(lambda: value)


# Generated at 2022-06-14 04:19:23.254911
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail('Error').to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:26.713358
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy method of Validation.

    >>> from pymonet.validation import Validation
    >>> validation = Validation(1, [])
    >>> lazy = validation.to_lazy()
    >>> assert lazy == Lazy(lambda: 1)
    """
    pass


# Generated at 2022-06-14 04:19:30.526502
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.fail(['as']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:19:34.830580
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def test_unit():
        return 'Success'

    assert Lazy(lambda: test_unit()).value == Validation.success('Success').to_lazy().value()


# Generated at 2022-06-14 04:19:38.658267
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def same(left, right):
        assert left == right

    same(Validation.success(1).to_lazy().get(), 1)
    same(Validation.fail([]).to_lazy().get(), None)


# Generated at 2022-06-14 04:19:42.142440
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Unit tests for method to_try of class Validation

# Generated at 2022-06-14 04:19:44.846651
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def f(v):
        return v
    assert Validation.success(1).to_lazy().eval(f) == 1
    assert Validation.fail(1).to_lazy().eval(f) == None



# Generated at 2022-06-14 04:19:49.737150
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:54.843858
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad import bind

    def mapper(value):
        return value

    def folder(value):
        from pymonet.monad import bind
        from pymonet.list_monad import List

        def inner_mapper(value):
            return List(value)

        return bind(value, inner_mapper)

    assert bind(Validation.success(2), mapper).to_lazy() == bind(Validation.success(2), mapper).to_try().to_lazy()
    assert bind(Validation.success(2), folder).to_lazy() == bind(Validation.success(2), folder).to_lazy()

# Generated at 2022-06-14 04:20:06.520151
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().run() == 1
    assert Validation.fail(1).to_lazy().run() == None


# Generated at 2022-06-14 04:20:10.833972
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    v = Validation.fail(1)
    l = v.to_lazy()
    assert type(l) == Lazy
    assert l.value() == None
    try:
        l.error()
        assert False
    except AttributeError:
        pass


# Generated at 2022-06-14 04:20:16.203576
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    success_validation = Validation.success(42)
    failure_validation = Validation.fail(['error1', 'error2'])

    assert success_validation.to_lazy() == Lazy(lambda: 42)
    assert failure_validation.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:20:19.477632
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    v1 = Validation(1, [])
    v2 = Validation(None, 'Something bad happened!')

    assert v1.to_lazy().value() == 1
    assert v2.to_lazy().value() == None


# Generated at 2022-06-14 04:20:29.097935
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation to_lazy() method should return Lazy monad with function that returns Validation value
    """
    from pymonet.identity import Identity
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    success = Validation.success(Identity(1))
    fail = Validation.fail([1, '2', 3.3, ['a'], {'b': 'c'}])

    assert success.to_lazy() == Lazy(lambda: Identity(1))
    assert fail.to_lazy() == Lazy(lambda: None)
    assert success.to_lazy().get() == Try(Identity(1), is_success=True)
    assert fail.to_lazy().get() == Try(None, is_success=False)

#

# Generated at 2022-06-14 04:20:34.621470
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # we have Lazy monad with function returning 1
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().force() == 1


# Generated at 2022-06-14 04:20:38.509984
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:43.246751
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Should return successful Try
    assert Lazy(lambda: 100) == Validation.success(100).to_lazy()
    # Should return failed Try
    assert Lazy(lambda: None) == Validation.fail().to_lazy()


# Generated at 2022-06-14 04:20:47.114268
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Create Lazy monad from Validation instance."""
    from pymonet.maybe import Maybe
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2).eval() == Lazy(lambda: Maybe(2)).unwrap().eval()

# Generated at 2022-06-14 04:20:51.086748
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    v = Validation.success(5)
    assert v.to_lazy() == Lazy(lambda: 5)

    v = Validation.fail()
    assert v.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:21:15.185290
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert_that(
        Validation.success().to_lazy(),
        equal_to(Lazy(lambda: None))
    )

# Generated at 2022-06-14 04:21:20.756223
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.functor.functor import Functor

    # Arrange
    functor = Functor(Lazy(lambda: 1))
    validation = Validation(1, [])

    # Act
    result = validation.to_lazy()

    # Assert
    expected = Lazy(lambda: 1)
    assert result == expected

# Generated at 2022-06-14 04:21:22.667064
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(5).to_lazy().value() == 5
    assert Validation.fail([1, 2, 3]).to_lazy().value() is None

# Generated at 2022-06-14 04:21:27.006730
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def innner_fnc():
        return 5

    validation = Validation.success(innner_fnc)
    lazy_val = validation.to_lazy()
    assert lazy_val.unbox()() == 5
