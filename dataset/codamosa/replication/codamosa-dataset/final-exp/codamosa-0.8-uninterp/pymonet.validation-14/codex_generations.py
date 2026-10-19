

# Generated at 2022-06-14 04:11:31.809100
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Validation.fail(['bar']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:11:35.355257
# Unit test for method __str__ of class Validation
def test_Validation___str__():
    assert str(Validation.success(1)) == 'Validation.success[1]'
    assert str(Validation.fail([1])) == 'Validation.fail[None, [1]]'


# Generated at 2022-06-14 04:11:38.519516
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().evaluate() == 1
    assert Validation.fail([]).to_lazy().evaluate() is None


# Generated at 2022-06-14 04:11:43.200719
# Unit test for method __str__ of class Validation
def test_Validation___str__():
    validation_success = Validation.success('test')
    validation_fail = Validation.fail(['test1', 'test2'])
    assert 'Validation.success[test]' == str(validation_success)
    assert 'Validation.fail[None, [\'test1\', \'test2\']]' == str(validation_fail)


# Generated at 2022-06-14 04:11:47.086499
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Checks that to_lazy function works correctly."""
    lazy = Validation.success(1).to_lazy()
    assert lazy.is_value
    assert lazy.value() == 1

    lazy = Validation.fail([1, 2]).to_lazy()
    assert lazy.is_value
    assert lazy.value() is None


# Generated at 2022-06-14 04:11:52.165357
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    fn = lambda x: 3
    success = Validation.success(1)
    fail = Validation.fail([])

    assert success.to_lazy() == Lazy(fn)
    assert fail.to_lazy() == Lazy(fn)

# Generated at 2022-06-14 04:11:56.852573
# Unit test for method __str__ of class Validation
def test_Validation___str__():
    """Unit test for method __str__ of class Validation"""
    assert str(
        Validation(value='foo', errors=['error'])) == 'Validation.fail[foo, [\'error\']]'
    assert str(
        Validation(value='foo', errors=[])) == 'Validation.success[foo]'


# Generated at 2022-06-14 04:12:05.132667
# Unit test for method __str__ of class Validation
def test_Validation___str__():
    from pymonet.maybe import Maybe, MaybeError
    from pymonet.either import Either, EitherError
    from pymonet.lazy import Lazy
    from pymonet.monad_list import List
    from pymonet.monad_try import Try
    from pymonet.monad_set import Set, SetError
    from pymonet.monad_dict import Dict, DictError

    assert Validation.success(100).__str__() == 'Validation.success[100]'
    assert Validation.success(Maybe.just(100)).__str__() == 'Validation.success[Maybe.just[100]]'
    assert Validation.success(Maybe.nothing()).__str__() == 'Validation.success[Maybe.nothing]'

# Generated at 2022-06-14 04:12:09.346393
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.monad_lazy import Lazy

    assert Validation.success('success').to_lazy() == Lazy(lambda: 'success')
    assert Validation.fail(['fail']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:14.670528
# Unit test for method __str__ of class Validation
def test_Validation___str__():
    success = Validation.success('value')
    assert(str(success) == 'Validation.success[value]')

    fail = Validation.fail(['first', 'second'])
    assert(str(fail) == 'Validation.fail[None, [\'first\', \'second\']]')


# Generated at 2022-06-14 04:12:19.477159
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().eval() == 1


# Generated at 2022-06-14 04:12:24.900891
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    lazy = Validation.success(5).to_lazy()
    assert isinstance(lazy, Lazy)
    assert isinstance(lazy.get(), Maybe)
    assert lazy.get().is_just()
    assert lazy.get().maybe_value() == 5

# Generated at 2022-06-14 04:12:31.635724
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:12:36.226165
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.fail(errors=[1, 2]).to_lazy()
    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()


# Generated at 2022-06-14 04:12:39.710795
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 1

    assert Validation.success(1).to_lazy() == Lazy(func)

# Generated at 2022-06-14 04:12:43.378143
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    lazy = Validation.success(40).to_lazy()
    r = lazy.get()
    assert r == 40

    lazy = Validation.fail().to_lazy()
    r = lazy.get()
    assert r == None


# Generated at 2022-06-14 04:12:48.733656
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    result = Validation(3, []).to_lazy()

    assert isinstance(result, Lazy)
    assert result() == 3

    result = Validation.fail([2]).to_lazy()

    assert isinstance(result, Lazy)
    assert result() is None


# Generated at 2022-06-14 04:12:50.521841
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:12:52.810771
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(2).to_lazy() == Validation.fail([]).to_lazy()


# Generated at 2022-06-14 04:12:55.523107
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(1, []).to_lazy().run() == 1


# Generated at 2022-06-14 04:13:08.544012
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    success = Validation.success(1)
    v1 = success.to_lazy()

    fail = Validation.fail([1, 2, 3])
    v2 = fail.to_lazy()

    assert isinstance(v1, Lazy)
    assert isinstance(v2, Lazy)
    assert v1.get_value() == 1
    assert v2.get_value() is None

    # None as value
    success = Validation.success()
    v1 = success.to_lazy()

    fail = Validation.fail([])
    v2 = fail.to_lazy()

    assert isinstance(v1, Lazy)
    assert isinstance(v2, Lazy)
    assert v1.get_value() is None
    assert v2.get_value() is None

# Unit test

# Generated at 2022-06-14 04:13:12.269402
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:18.708868
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(value='Hello').to_lazy() == Lazy(lambda: 'Hello')
    assert Validation.fail(errors=['Invalid data']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(value='Ok').is_success() == True
    assert Validation.fail(errors=['Invalid data']).is_success() == False
    assert Validation.success(value='Ok').to_try() == Try('Ok')
    assert Validation.fail(errors=['Invalid data']).to_try() == Try(None, is_success=False)


# Generated at 2022-06-14 04:13:23.657110
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def validation_to_lazy(value):
        return Validation.success(value).to_lazy()

    assert validation_to_lazy(1) == Lazy(lambda: 1)


# Generated at 2022-06-14 04:13:24.797014
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')


# Generated at 2022-06-14 04:13:28.309217
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    v = Validation.success(1)
    assert v.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:13:31.805601
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')
    assert Validation.fail(['not null']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:42.713640
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """
    Test for method to_lazy of class Validation
    """
    def assert_Validation_is_lazy(validation):
        """
        Assert that Validation is lazy

        :param validation: tested validation
        :type validation: Validation
        """
        def assert_Validation_not_lazy():
            """
            Assert that Validation is not lazy
            """
            assert validation == Validation.fail(['Value accessed before calculation'])

        validation.to_try()
        assert_Validation_not_lazy()
        validation.to_lazy()
        assert_Validation_not_lazy()
        validation.to_maybe()
        assert_Validation_not_lazy()
        validation.to_either()
        assert_Validation_not_lazy()

# Generated at 2022-06-14 04:13:45.459404
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success('value').to_lazy()
    assert lazy == Lazy(lambda: 'value')


# Generated at 2022-06-14 04:13:47.963409
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    assert Validation.success(123).to_lazy() == Lazy(lambda: 123)


# Generated at 2022-06-14 04:13:52.310043
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 04:13:56.610484
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    res = Validation.fail(['error']).to_lazy()
    assert res == Lazy(lambda: None)
    res = Validation.success(1).to_lazy()
    assert res == Lazy(lambda: 1)


# Generated at 2022-06-14 04:14:01.426480
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def value_func():
        return 42

    lazy_validation = Validation.success(value_func).to_lazy()
    assert isinstance(lazy_validation, Lazy)
    assert lazy_validation.evaluate() == 42


# Generated at 2022-06-14 04:14:08.759924
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    val = Validation('a', [])
    lazy = val.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == val.value

    val = Validation('a', ['a'])
    lazy = val.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value() == val.value


# Generated at 2022-06-14 04:14:11.773786
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given
    value = 1
    validation = Validation(value, [])
    # When
    result = validation.to_lazy()
    # Then
    assert result == Lazy(lambda: value)


# Generated at 2022-06-14 04:14:15.539849
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    @Lazy
    def hello_world():
        return 'hello world'

    assert hello_world == Lazy(lambda: 'hello world'), 'Should convert lazy to lazy'

# Generated at 2022-06-14 04:14:25.402309
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    class TestSuccess:
        @classmethod
        def success(cls):
            return Validation.success(1)

    class TestFail:
        @classmethod
        def fail(cls):
            return Validation.fail(["error"])

    assert isinstance(TestSuccess.success().to_lazy(), Lazy)
    assert isinstance(TestFail.fail().to_lazy(), Lazy)
    assert TestSuccess.success().to_lazy().get() == TestSuccess.success().value
    assert TestFail.fail().to_lazy().get() == TestFail.fail().value



# Generated at 2022-06-14 04:14:28.423551
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    lazy = Lazy(lambda: 6)
    assert Validation.success(6).to_lazy() == lazy

# Generated at 2022-06-14 04:14:35.259088
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def tester(fn):
        return fn()

    # Test Lazy[Function() -> (A | None)] returned by method to_lazy when Validation has no errors
    assert tester(Validation.success(5).to_lazy()) == 5

    # Test Lazy[Function() -> (A | None)] returned by method to_lazy when Validation has errors
    assert tester(Validation.fail(5).to_lazy()) == None

# Generated at 2022-06-14 04:14:38.867135
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'string') == Validation('string', []).to_lazy()


# Generated at 2022-06-14 04:14:46.555207
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    u"""
    Checks if Validation is transformed to Lazy successfuly
    """
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 04:14:51.313200
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    val1 = Validation(1, [])
    val2 = Validation(None, [])
    lazy1 = val1.to_lazy()
    lazy2 = val2.to_lazy()
    assert lazy1.get() == 1
    assert lazy2.get() == None


# Generated at 2022-06-14 04:14:54.767095
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(42).to_lazy().memoize().value == 42
    assert Validation.fail(['error']).to_lazy().memoize().value is None



# Generated at 2022-06-14 04:15:01.319944
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.

    """
    try:
        assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
        assert Validation.fail(errors=['e1']).to_lazy() == Lazy(lambda: None)
    except AssertionError as error:
        print("In test 'test_Validation_to_lazy' error occurred: {}".format(error))
        raise error


# Generated at 2022-06-14 04:15:09.555305
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_try import Success, Failure

    # Given: Successful Validation
    validation = Validation.success(1)

    # When: to_lazy called
    value = validation.to_lazy()

    # Then: Lazy monad is returned
    assert isinstance(value, Lazy)

    # And: Lazy monad is Success
    assert isinstance(value.get(), Success)



# Generated at 2022-06-14 04:15:12.278930
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:23.590888
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    empty = Validation.success()
    lazy = empty.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == empty.value

    success = Validation.success(2)
    lazy = success.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == success.value

    fail = Validation.fail()
    lazy = fail.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == fail.value

    fail = Validation.fail(['error'])
    lazy = fail.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == fail.value


# Generated at 2022-06-14 04:15:26.779716
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:15:31.743434
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.success(None).to_lazy() != Lazy(lambda: 5)
    assert Validation.fail(['a']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:34.183950
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Validation(Box(4), []).to_lazy() == Lazy(lambda: Box(4))

# Generated at 2022-06-14 04:15:48.339359
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validate_one = Validation.success(1)
    validate_two = Validation.fail([2])

    monad_lazy_one = validate_one.to_lazy()
    monad_try_one = validate_one.to_try()
    monad_lazy_two = validate_two.to_lazy()
    monad_try_two = validate_two.to_try()

    assert monad_lazy_one.eval() == 1
    assert isinstance(monad_lazy_one.result(), Try)
    assert monad_lazy_one.result() == monad_try_one

    assert monad_lazy_two.eval() == None

# Generated at 2022-06-14 04:15:54.820903
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(value=10).to_lazy() == Lazy(function=lambda: 10)
    assert Validation.success(value=None).to_lazy() == Lazy(function=lambda: None)
    assert Validation.fail(errors=[ValidationError('test')]).to_lazy() == Lazy(function=lambda: None)


# Generated at 2022-06-14 04:15:59.790161
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    val = Validation.success(1)
    assert val.to_lazy() == Lazy(lambda: 1)

    val2 = Validation.fail('error')
    assert val2.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:03.308379
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()



# Generated at 2022-06-14 04:16:06.549005
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    v = Validation.success(5).to_lazy()
    assert v == Lazy(lambda: 5)


# Generated at 2022-06-14 04:16:09.717037
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:16:14.064300
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)
    assert Validation(1, []).to_lazy().get_value() == 1


# Generated at 2022-06-14 04:16:17.875409
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().get() == 1
    assert Validation.fail(['error']).to_lazy().get() is None
    assert Validation.fail(['error']).to_lazy().get() is None


# Generated at 2022-06-14 04:16:23.961881
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    success = Validation.success(42)
    assert Lazy(lambda: 42) == success.to_lazy()

    fail = Validation.fail(['error1', 'error2'])
    assert Lazy(lambda: None) == fail.to_lazy()


# Generated at 2022-06-14 04:16:30.428392
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Take function and applied this function on current Validation value and returns folder result.

    :param mapper: mapper function
    :type mapper: Function(A) -> Validation[B, E]
    :returns: new Validation with mapped value
    :rtype: Validation[B, E]
    """
    from pymonet.lazy import Lazy

    assert Validation(10, []).to_lazy() == Lazy(lambda: 10)

# Generated at 2022-06-14 04:16:44.078841
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def get_num():
        return 1

    validation = Validation(1, [])

    assert Lazy(get_num) == validation.to_lazy()



# Generated at 2022-06-14 04:16:49.199681
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    result_success = Validation.success(1).to_lazy()
    result_fail = Validation.fail([1]).to_lazy()

    assert isinstance(result_success, Lazy)
    assert isinstance(result_fail, Lazy)
    assert result_success.get() == 1
    assert result_fail.get() is None


# Generated at 2022-06-14 04:16:56.440019
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.utils import identity

    assert Validation.success(Try.fail(1)).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(identity)(1)
    assert Validation.fail('error').to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:00.990959
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 10)
    assert Validation.success(10).to_lazy() == lazy
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:07.262114
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monads.validation import Validation
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Lazy(lambda: 1).to_validation().is_success()
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)
    assert Lazy(lambda: None).to_validation().is_fail()


# Generated at 2022-06-14 04:17:13.371046
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    def function_creating_Try(value):
        if value == 'x':
            return Try(None, False)
        return Try(value)

    assert function_creating_Try('a').to_validation().to_lazy() | function_creating_Try('x').to_validation().to_lazy() == \
        Validation.success('a').to_lazy() | Validation.fail().to_lazy()



# Generated at 2022-06-14 04:17:18.051341
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    def _test(method_name, expected_result, *args):
        """Test given method of class Validation"""
        from pymonet.monad_try import Success

        actual_result = getattr(Validation.success(*args), method_name)()
        assert expected_result == actual_result
        assert actual_result.monad == Success

    _test('to_lazy', Validation.success(), 5)



# Generated at 2022-06-14 04:17:21.066123
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:25.350212
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:17:30.655160
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    success_value = Try(lambda: 10)
    validation = Validation.success(success_value)
    assert validation.to_lazy()(lambda: None) == success_value

    def f():
        raise ArithmeticError('Division by zero')
        return 10

    failed_value = Try(f)
    validation = Validation.fail([failed_value])
    assert validation.to_lazy()(lambda: None) == failed_value



# Generated at 2022-06-14 04:17:56.063190
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.functor import Functor
    from pymonet.monad_try import Try
    from pymonet.monad_lazy import Lazy

    # Test is_fail function
    assert Validation.success(5).to_maybe().is_just()

    # Test is_fail function
    assert Validation.fail(['error', 'error']).to_maybe().is_nothing()

    v = Validation.success(lambda x: x + 2)
    assert Lazy.unit(lambda: 5).ap(v).value() == 7
    assert Validation.fail(["fail"]).to_lazy().ap(v).is_fail() == True

    assert Lazy.unit(10).ap(Validation.success(lambda x: x + 2)).value() == 12

# Generated at 2022-06-14 04:17:59.333130
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box

    assert Lazy(lambda: Box('hello')) == Validation.success(Box('hello')).to_lazy()


# Generated at 2022-06-14 04:18:03.675926
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert_that(Validation.success(2).to_lazy(), equal_to(Lazy(lambda: 2)))
    assert_that(Validation.fail([]).to_lazy(), equal_to(Lazy(lambda: None)))



# Generated at 2022-06-14 04:18:06.044061
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 04:18:12.296535
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail().to_lazy()
    assert Lazy(lambda: None) == Validation.fail(['Error']).to_lazy()


# Generated at 2022-06-14 04:18:16.260463
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.success(10)

    assert validation.to_lazy() == Lazy(lambda: 10)

    validation = Validation.fail([10, 20, 30])

    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:27.812351
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.monad_try import Success
    from pymonet.monad_try import Failure
    from pymonet.monad_try import FailureWithException

    assert Lazy(lambda: Validation.success(1).to_lazy()).force() == 1
    assert Lazy(lambda: Validation.fail().to_lazy()).force() is None

    assert Lazy(lambda: Validation.success(1).to_lazy().force()).force() == 1
    assert Lazy(lambda: Validation.fail().to_lazy().force()).force() is None

    assert Lazy(lambda: Validation.success(1).to_lazy().to_try()).force() == Success(1)
   

# Generated at 2022-06-14 04:18:29.309117
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(2, []).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 04:18:38.196579
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    val = Validation(1, [])
    assert val.to_lazy() == Lazy(lambda: 1)

    val = Validation(1, [2])
    assert val.to_lazy() == Lazy(lambda: 1)

    val = Validation(None, [])
    assert val.to_lazy() == Lazy(lambda: None)

    val = Validation(None, [2])
    assert val.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:46.550597
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Success, Failure
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    validate = Validation(42, ['error'])
    validate2 = Validation(42, [])
    validate_lazy = validate.to_lazy()
    validate2_lazy = validate2.to_lazy()

    # test to_box
    assert validate.to_box() == Box(42)
    assert validate2.to_box() == Box(42)

    # test to_maybe
    assert validate.to_maybe() == Maybe.nothing()
    assert validate2.to_maybe() == Maybe.just(42)

    # test to_try
    assert validate.to_try() == Success(42)

# Generated at 2022-06-14 04:19:25.990123
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.monad_lazy import Lazy
    from pymonet.monad_validation import Validation

    success = 10
    Validation.success(success).to_lazy() == Lazy(lambda: success)
    Validation.success(success).to_lazy() == Lazy(lambda: success)


# Generated at 2022-06-14 04:19:32.946467
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(1)
    assert validation.to_lazy().get() == 1
    assert validation.to_lazy().is_just() == True
    assert validation.to_lazy().is_nothing() == False

    validation = Validation.fail()
    assert validation.to_lazy().get() is None
    assert validation.to_lazy().is_just() == False
    assert validation.to_lazy().is_nothing() == True



# Generated at 2022-06-14 04:19:43.981833
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.functors import Functor
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left

    def print_lazy(lazy):
        print(lazy())

    def print_validation(validation):
        try:
            print(validation())
        except Exception as e:
            print(e)

    def print_try(try_):
        try:
            print(try_())
        except Exception as e:
            print(e)

    def print_either(either):
        try:
            print(either())
        except Exception as e:
            print(e)

    success_val = Validation.success(value=1)
    fail_val = Validation.fail(errors=['error'])

# Generated at 2022-06-14 04:19:50.542150
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Compare lazily evaluated value with not lazily evaluated value.
    """
    from pymonet.box import Box

    assert Validation.success(Box(1)).to_lazy().monad().value == Validation.success(Box(1)).value
    assert Validation.fail(Box(1)).to_lazy().monad().value == Validation.fail(Box(1)).value


# Generated at 2022-06-14 04:19:53.849688
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().get() == 1


# Generated at 2022-06-14 04:19:59.813508
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    def func():
        return 'value'

    validation = Validation.success(func())
    lazy = validation.to_lazy()
    test.assert_equals('value', lazy.eval())

    lazy2 = Validation.fail([]).to_lazy()
    test.assert_equals(None, lazy2.eval())


# Generated at 2022-06-14 04:20:03.975214
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    import pymonet.validation as validation

    assert Lazy(lambda: 1) == validation.Validation(1, []).to_lazy()


# Generated at 2022-06-14 04:20:07.292939
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    value = Validation.success(lambda x: x).to_lazy().value()
    assert callable(value)

    assert Validation.fail(lambda x: x).to_lazy().value() is None

# Generated at 2022-06-14 04:20:10.875077
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    assert Validation.success('hello').to_lazy() == Lazy(lambda: 'hello')
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:16.204877
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    >>> test_Validation_to_lazy()
    True
    """
    from pymonet.lazy import Lazy

    validation = Validation.success(True)
    lazy = validation.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.evaluate() == True
