

# Generated at 2022-06-14 04:11:33.345902
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Validation.fail(['error'])
    assert val.to_lazy() == Lazy(lambda: None)
    val = Validation.success(12)
    assert val.to_lazy() == Lazy(lambda: 12)

# Generated at 2022-06-14 04:11:37.847668
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    assert Maybe.just('a').to_lazy().value() == 'a'
    assert Try(1, True).to_lazy().value() == 1
    assert Try(1, False).to_lazy().value() is None


# Generated at 2022-06-14 04:11:43.977852
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    It checks that Validation is transformed to Lazy monad.
    """
    from pymonet.lazy import Lazy

    x = Validation.success(2)
    y = x.to_lazy()
    assert y == Lazy(lambda: 2)
    assert y.value() == 2
    assert y.is_computed() == False
    y.value()
    assert y.is_computed() == True


# Generated at 2022-06-14 04:11:49.226039
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    import pymonet.monad_either as Either
    import pymonet.monad_try as Try

    def _validation_to_lazy():
        validation = Validation.success('value')
        lazy = validation.to_lazy()
        return (validation, lazy)

    validation, lazy = _validation_to_lazy()
    assert validation == Validation.success('value')
    assert lazy == Lazy(lambda: 'value')
    assert Either.validate_lazy(lazy).is_success()
    assert Try.validate_lazy(lazy).is_success()


# Generated at 2022-06-14 04:11:54.726227
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # given
    a = Validation.success(10)

    # when
    lazy = a.to_lazy()

    # then
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 10


# Generated at 2022-06-14 04:11:58.014886
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    val = Validation(10, [])

    lazy = val.to_lazy()

    assert lazy == Lazy(lambda: 10)


# Generated at 2022-06-14 04:12:05.014829
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Validation.success(Try(1, is_success=True)).to_lazy() == Lazy(lambda: Try(1, is_success=True))
    assert Validation.success(Try(1, is_success=False)).to_lazy() == Lazy(lambda: Try(1, is_success=False))
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:08.656754
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.fail(['error-1', 'error-2']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:12:11.351061
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:16.657372
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """It tests method 'to_lazy' of class Validation"""

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:22.986577
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    valid = Validation.success(10)
    assert valid.to_lazy() == Lazy(lambda: Box(10))


# Generated at 2022-06-14 04:12:26.376680
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == 1


# Generated at 2022-06-14 04:12:34.732028
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test to_lazy method of class Validation."""
    from pymonet.lazy import Lazy

    lazy = Validation.success(5).to_lazy()

    assert isinstance(lazy, Lazy)
    assert callable(lazy.lazy_value)
    assert lazy.lazy_value() == 5

    lazy = Validation.fail([1, 2, 3]).to_lazy()

    assert isinstance(lazy, Lazy)
    assert not callable(lazy.lazy_value)
    assert lazy.lazy_value is None

    class ExceptionClass:
        pass

    lazy = Validation.fail([ExceptionClass()]).to_lazy()

    assert isinstance(lazy, Lazy)
    assert not callable(lazy.lazy_value)

# Generated at 2022-06-14 04:12:40.061896
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Validation.fail(['Boom']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:44.774511
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail().to_lazy()
    assert repr(Lazy(lambda: None)) == repr(Validation.fail().to_lazy())


# Generated at 2022-06-14 04:12:47.624640
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    def mapper(value):
        return "Some value"
    assert Lazy(mapper) == Validation.success(1).to_lazy().map(mapper)


# Generated at 2022-06-14 04:12:53.465474
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def mapper(i): # pragma: no cover
        return i + 1

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['err']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy().map(mapper) == Lazy(lambda: 2)


# Generated at 2022-06-14 04:12:59.938818
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(errors=['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:10.805611
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    val = Validation.success(42)

    lazy_val = val.to_lazy()
    assert lazy_val.func() == 42
    assert lazy_val.is_lazy()
    assert lazy_val.is_forced()
    assert lazy_val.eval() == 42

    val = Validation.success([1, 2, 3])
    lazy_val = val.to_lazy()
    assert lazy_val.func() == [1, 2, 3]
    assert lazy_val.is_lazy()
    assert lazy_val.is_forced()
    assert lazy_val.eval() == [1, 2, 3]


# Generated at 2022-06-14 04:13:16.902247
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from hypothesis import given, strategies as st

    from pymonet.monad_try import Try
    from pymonet.lazy import *

    @given(st.text())
    def test_to_lazy(text):
        validation = Validation.success(text)
        lazy = validation.to_lazy()

        assert isinstance(lazy, Lazy)
        assert isinstance(lazy.eval(), Validation)
        assert isinstance(lazy.eval(), Try)
        assert lazy.eval() == validation


# Generated at 2022-06-14 04:13:24.043144
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    value = 1
    validation = Validation.success(value)
    assert validation.to_lazy() == Lazy(lambda: value)


# Generated at 2022-06-14 04:13:27.642217
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 04:13:30.066326
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy = Validation.success('alpha').to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.value() == 'alpha'


# Generated at 2022-06-14 04:13:35.241380
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation_success = Validation.success('success')
    l = validation_success.to_lazy()
    assert l.get() == 'success'

    validation_fail = Validation.fail(['fail'])
    l = validation_fail.to_lazy()
    assert l.get() is None


# Generated at 2022-06-14 04:13:37.369352
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def f():
        return 3

    assert Validation.success(3).to_lazy() == Lazy(f)

# Generated at 2022-06-14 04:13:39.974215
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    result = Validation.success(10)
    assert result.to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 04:13:44.437016
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    try_lazy = Try(lazy, is_success=True)
    assert isinstance(try_lazy, Try)
    assert try_lazy.is_success()
    assert isinstance(try_lazy.value, Lazy)
    assert try_lazy.value() == 1


# Generated at 2022-06-14 04:13:49.783876
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    f = lambda: Maybe.just(2)

    m = Lazy(f)

    monad = Validation.success().map(m)
    assert monad.value.is_just()
    assert monad.value() == Maybe.just(2)


# Generated at 2022-06-14 04:13:52.793708
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def fun():
        return "val"

    lazy = Validation.success(fun).to_lazy()
    assert lazy == Lazy(fun)



# Generated at 2022-06-14 04:13:55.588071
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    data = { 'test': 'test' }
    validation = Validation.success(data)
    assert(validation.to_lazy().get() == data)

# Generated at 2022-06-14 04:14:02.300317
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Test method Validation.to_lazy, transform Validation to Lazy"""
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy = Validation.success(42).to_lazy()

    assert lazy == Lazy(lambda: 42)


# Generated at 2022-06-14 04:14:10.351284
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    left = Validation(None, [1, 2, 3]).to_lazy()
    assert isinstance(left, Lazy)
    assert isinstance(left.exe(), Try)
    assert left.exe().is_fail()

    right = Validation(2, []).to_lazy()
    assert isinstance(right, Lazy)
    assert isinstance(right.exe(), Try)
    assert right.exe().is_success()

# Generated at 2022-06-14 04:14:13.256758
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_lazy import Lazy
    from pymonet.validation import Validation

    a = Validation(1, [])
    b = a.to_lazy()

    assert isinstance(b, Lazy)
    assert b.call() == 1


# Generated at 2022-06-14 04:14:17.544999
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    assert lazy == Lazy(lambda: 1)

# Unit tests for method to_try of class Validation

# Generated at 2022-06-14 04:14:22.018617
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:24.253819
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().get() == 1



# Generated at 2022-06-14 04:14:27.421511
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test Validation to_lazy method
    """
    assert Validation.success(100).to_lazy().get() == 100



# Generated at 2022-06-14 04:14:30.507127
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    lazy_success = Lazy(lambda: 10)
    assert Validation.success(10).to_lazy() == lazy_success


# Generated at 2022-06-14 04:14:39.862032
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def assert_to_lazy(validation, expected_value, expected_is_computed):
        lazy = validation.to_lazy()
        assert isinstance(lazy, Lazy)
        assert lazy.value() == expected_value
        assert lazy.is_computed == expected_is_computed

    error = 'error'
    success = 'success'
    assert_to_lazy(Validation.success(success), success, False)
    assert_to_lazy(Validation.fail([error]), None, False)


# Generated at 2022-06-14 04:14:40.903828
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Arrange
    validation = Validation.success(123)

    # Act
    lazy = validation.to_lazy()

    # Assert
    assert lazy.get() == 123

# Generated at 2022-06-14 04:14:46.816768
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    def test1():
        return Validation.success(True)

    def test2():
        return Validation.success(None)

    assert test1().to_lazy().value() == True
    assert test2().to_lazy().value() == None



# Generated at 2022-06-14 04:14:53.693536
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test_Validation_to_lazy_0():
        assert Validation.success(value=1).to_lazy() == Lazy(lambda: 1)

    def test_Validation_to_lazy_1():
        assert Validation.fail(errors=[1, 2]).to_lazy() == Lazy(lambda: None)

    test_Validation_to_lazy_0()
    test_Validation_to_lazy_1()


# Generated at 2022-06-14 04:14:58.365395
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:04.633367
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert (Validation.success(42).to_lazy() ==
            Lazy(lambda: 42) == Lazy.unit(42))
    assert (Validation.fail(['error']).to_lazy() ==
            Lazy(lambda: None) == Lazy.unit(None))


# Generated at 2022-06-14 04:15:08.575268
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.validation import Validation

    result = Validation.success("test").to_lazy()
    assert result.run() == "test"

    result = Validation.fail("test").to_lazy()
    assert result.run() is None



# Generated at 2022-06-14 04:15:11.588462
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(1).to_lazy().evaluate() == Lazy(lambda: 1).evaluate()
    assert Validation.fail(['error']).to_lazy().evaluate() is None

# Generated at 2022-06-14 04:15:16.033595
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:20.428316
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.success(3)
    lazy = validation.to_lazy()
    assert validation == Validation.success(lazy.eval())
    assert isinstance(lazy, Lazy)


# Generated at 2022-06-14 04:15:30.512628
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.box import Box

    assert Validation.success('Hey!').to_lazy() == Lazy(lambda: 'Hey!')
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.success([1, 2, 3]).map(lambda x: x + [4]).to_lazy() == Lazy(lambda: [1, 2, 3, 4])

    assert Validation.fail([1, 2, 3]).to_maybe() == Maybe.nothing()
    assert Validation.success('Hey!').to_maybe() == Maybe.just('Hey!')
   

# Generated at 2022-06-14 04:15:33.617928
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

# Generated at 2022-06-14 04:15:38.580177
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Validation.success(Box(True)).to_lazy() == Lazy(lambda: Box(True))


# Generated at 2022-06-14 04:15:47.544351
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.functor import Functor
    from pymonet.monad import Monad
    from pymonet.alternative import Alternative
    from pymonet.monad_plus import MonadPlus
    from pymonet.chain import Chain

    assert isinstance(Validation.success(1).to_lazy(), Functor)
    assert isinstance(Validation.success(1).to_lazy(), Monad)
    assert isinstance(Validation.success(1).to_lazy(), Alternative)
    assert isinstance(Validation.success(1).to_lazy(), MonadPlus)
    assert isinstance(Validation.success(1).to_lazy(), Chain)



# Generated at 2022-06-14 04:15:52.454246
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    success = Validation.success('foo')
    fail = Validation.fail(['bar'])

    assert success.to_lazy() == Lazy(lambda: 'foo')
    assert fail.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:16:00.842489
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:16:04.750990
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def lazy():
        return 4

    assert Validation.success(value=lazy()).to_lazy().get() == 4
    assert Validation.fail(errors=['error']).to_lazy().get() is None


# Generated at 2022-06-14 04:16:06.425300
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Lazy(lambda: 'a') == Validation.success('a').to_lazy()


# Generated at 2022-06-14 04:16:09.613923
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success('some value').to_lazy() == Lazy(lambda: 'some value')
    assert Validation.success('other value').to_lazy()._function() == 'other value'


# Generated at 2022-06-14 04:16:15.548001
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('').to_lazy() == Lazy(lambda: '')
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 04:16:21.373548
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """ Unit test for method to_lazy of class Validation """
    value, errors = 'value', ['error']
    success_validation = Validation.success(value)
    fail_validation = Validation.fail(errors)

    assert isinstance(success_validation.to_lazy(), Lazy)
    assert success_validation.to_lazy() == Lazy(lambda: value)
    assert isinstance(fail_validation.to_lazy(), Lazy)
    assert fail_validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:28.315898
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([1,2,3]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(10).to_lazy().value() == 10
    assert Validation.fail([1,2,3]).to_lazy().value() == None


# Generated at 2022-06-14 04:16:38.522035
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def return_string():
        return 'string'

    assert Validation.success('string').to_lazy() == Lazy(return_string)
    assert Validation.success(1).to_lazy() != Lazy(return_string)
    assert Validation.fail(['error']).to_lazy() != Lazy(return_string)


# Generated at 2022-06-14 04:16:49.054668
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from nose_parameterized import parameterized
    from pymonet.test_utils import param_test

    @parameterized.expand([
        param_test((Validation.success('hello'), Lazy(lambda: 'hello'))),
        param_test((Validation.fail('bye'), Lazy(lambda: None)))
    ])
    def test_Validation_to_lazy(validation, expected_result):
        """
        Test method to_lazy of class Validation.
        """
        result = validation.to_lazy()
        assert result == expected_result



# Generated at 2022-06-14 04:16:53.867105
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation.success(Lazy(lambda: Box(1))).to_lazy() == \
        Lazy(lambda: Box(1))

# Generated at 2022-06-14 04:16:56.641688
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy_validation = Validation.success(10).to_lazy()
    assert lazy_validation == Lazy(lambda: 10)


# Generated at 2022-06-14 04:16:59.460417
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success().to_lazy() == Lazy(lambda: None)
    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 04:17:08.834783
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor

    validation = Validation.success(4)
    # 4 is not None and function in Lazy monad is called
    assert validation.to_lazy().map(lambda x: x > 3).get_or_else(False)
    # None is None and function in Lazy monad is called
    assert validation.to_lazy().map(lambda x: x > 4).get_or_else(False)
    # function in Lazy monad is called and returns Validation
    assert validation.to_lazy().map(lambda x: x > 4).map(lambda x: x == 4) == Lazy(lambda: False)


# Generated at 2022-06-14 04:17:11.225764
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:17:18.637444
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.either import Either
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Lazy(lambda: Maybe.just(4)) == Validation.success(4).to_lazy()
    assert Lazy(lambda: Maybe.just(6)) == Validation.success(6).to_lazy()
    assert Lazy(lambda: Either.right(8)) \
        == Validation.success(8).to_lazy()

    assert Lazy(lambda: Maybe.nothing()) == Validation.fail(['Error']).to_lazy()
    assert Lazy(lambda: Either.left(['23', '42'])) \
        == Validation.fail(['23', '42']).to_lazy()


# Generated at 2022-06-14 04:17:21.616377
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success('abc')
    lazy = validation.to_lazy()
    assert lazy == Lazy(lambda: 'abc')
    assert lazy.value() == 'abc'


# Generated at 2022-06-14 04:17:28.963981
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert (
        Validation.success(42)
        .to_lazy()
        .map(lambda x: x()) == Lazy(lambda: 42).map(lambda x: x())
    )

    assert (
        Validation.fail('something went wrong')
        .to_lazy()
        .map(lambda x: x()) == Lazy(lambda: None).map(lambda x: x())
    )



# Generated at 2022-06-14 04:17:39.316142
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def test():
        return (
            Validation.success(2)
            .to_lazy()
            .map(lambda x: x * x)
            .get()
        )

    assert test() == 4



# Generated at 2022-06-14 04:17:42.222361
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    def try_function():
        from pymonet.validation import Validation

        return Validation.success(23)

    from pymonet.lazy import Lazy

    lazy = Lazy(try_function)
    assert lazy.get().to_lazy() == lazy


# Generated at 2022-06-14 04:17:45.497677
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    success_validation = Validation.success(71)
    assert success_validation.to_lazy().get() == 71

    fail_validation = Validation.fail()
    assert success_validation.to_lazy().get() is None


# Generated at 2022-06-14 04:17:51.463913
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def return_val_4():
        return 4

    def return_val_err():
        return Validation.fail(['err'])

    assert Validation.success(4).to_lazy() == Lazy(return_val_4)
    assert Validation.fail(['err']).to_lazy() == Lazy(return_val_err)


# Generated at 2022-06-14 04:17:55.208938
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail(['error']).to_lazy()


# Generated at 2022-06-14 04:17:56.648333
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    v = Validation.success(10)
    l = v.to_lazy()
    assert l.get() == 10


# Generated at 2022-06-14 04:18:00.120660
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    validation = Validation.success('success')
    lazy_validation = validation.to_lazy()
    assert lazy_validation.get() == validation.value


# Generated at 2022-06-14 04:18:11.167995
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.function import compose, curry, map_
    from pymonet.lazy import Lazy
    from pymonet.monad_lazy import MonadLazy

    @curry
    def add1(val):
        return val + 1

    @curry
    def div2(val):
        return val / 2

    @curry
    def map_add1(monad):
        return map_(add1)(monad)

    @curry
    def bind_div2(monad):
        return MonadLazy.bind(div2)(monad)

    result = compose(bind_div2(map_add1(Lazy(1)))
                     , map_add1(bind_div2(Lazy(2)))
                     , Validation.to_lazy)(Validation.success(10))()


# Generated at 2022-06-14 04:18:16.980562
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    # Test with empty errors list
    success_lazy_1 = Validation.success(1).to_lazy()
    assert(success_lazy_1 == Lazy(lambda: 1))
    # Test with not empty errors list
    fail_lazy_1 = Validation.fail(['test']).to_lazy()
    assert(fail_lazy_1 == Lazy(lambda: None))


# Generated at 2022-06-14 04:18:22.381193
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:43.784374
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma : no cover
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(f=lambda: 5)
    assert Validation.success().to_lazy() == Lazy(f=lambda: None)
    assert Validation.fail(errors=[1, 2, 3]).to_lazy() == Lazy(f=lambda: None)


# Generated at 2022-06-14 04:18:45.737105
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation(True, [])
    assert validation.to_lazy() == Lazy(lambda: True)

# Generated at 2022-06-14 04:18:51.671376
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def to_lazy_success():
        assert Validation.success(4).to_lazy() == Lazy(lambda: 4)

    def to_lazy_fail():
        assert Validation.fail([]).to_lazy() == Lazy(lambda: None)

    to_lazy_fail()
    to_lazy_success()


# Generated at 2022-06-14 04:18:57.891271
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """
    Unit test for to_lazy method of Validation class.
    """
    from pymonet.lazy import Lazy

    def test(value):
        """
        Function to call from lazy value.
        """
        return value

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:19:02.396535
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation.success(Box(5)).to_lazy() == Lazy(lambda: Box(5))
    assert Validation.success().to_lazy() == Lazy(lambda: None)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:06.998307
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # given
    validation = Validation.success(5)

    # when
    lazy = validation.to_lazy()

    # then
    assert isinstance(lazy, Lazy)
    assert lazy.eval() == 5


# Generated at 2022-06-14 04:19:09.626911
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    expected = 'str'
    validation = Validation.success(expected)
    actual = validation.to_lazy().evaluate()
    assert expected == actual



# Generated at 2022-06-14 04:19:14.347504
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    value = 10
    v = Validation.success(value)
    res = v.to_lazy()
    assert res == Lazy(lambda: value)


# Generated at 2022-06-14 04:19:16.744875
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val1 = Validation.success(1)
    val2 = Validation.fail()

    assert isinstance(val1.to_lazy(), Lazy)
    assert isinstance(val2.to_lazy(), Lazy)
    assert val1.to_lazy().get() == 1
    assert val2.to_lazy().get() is None


# Generated at 2022-06-14 04:19:20.150474
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail(10).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:19:57.410913
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:20:01.860819
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.either import Right, Left
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([123]).to_lazy() == Lazy(lambda: None)

    assert Validation.success().to_lazy() == Lazy(lambda: None)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:05.595167
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.success('value').to_lazy()
    assert lazy.value() == 'value'

    lazy = Validation.fail(['error']).to_lazy()
    assert lazy.value() is None


# Generated at 2022-06-14 04:20:09.763380
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    def test_function(x):
        return Try(x)

    validation = Validation.success(2)
    assert validation.to_lazy().value() == test_function(2).value()


# Generated at 2022-06-14 04:20:13.599835
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test method to_lazy of class Validation.
    """
    assert Validation.success(1).to_lazy().run()(1)
    assert Validation.success(2).to_lazy().get() == 1
    assert Validation.fail(2).to_lazy().get()(2)
    assert Validation.fail(3).to_lazy().get() == 2

# Generated at 2022-06-14 04:20:21.017703
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test for method 'to_lazy' for Validation.
    """
    from pymonet.monad_try import Try
    from pymonet.monad_list import List

    v = Validation.success('a').to_lazy()
    assert isinstance(v.get(), str)
    assert v.get() == 'a'

    v = Validation.fail(List(['a', 'b']).map(lambda x: Try().fail(x)).to_list()).to_lazy()
    assert v.get() is None

# Generated at 2022-06-14 04:20:23.675949
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validate = Validation.success(2)
    assert validate.to_lazy().value() == 2

    validate = Validation.fail([])
    assert validate.to_lazy().value() == None


# Generated at 2022-06-14 04:20:28.624729
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy = Validation.fail().to_lazy()

    assert (Lazy(lambda: None) == lazy)

    lazy = Validation.success(1).to_lazy()

    assert (Lazy(lambda: 1) == lazy)


# Generated at 2022-06-14 04:20:29.964204
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    result = Validation.success(1).to_lazy()

    assert result.force() == 1


# Generated at 2022-06-14 04:20:34.177627
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    f = lambda: 'foo'
    assert Validation.success(f).to_lazy() == Lazy(f)
    assert Validation.success().to_lazy() == Lazy(None)